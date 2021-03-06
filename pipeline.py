import functions
import instructions_memory
import registerBase
import control
import ALUControl
import dataMemory
import ALU

def sign_extend(value):
    sign_bit = value[0]
    extend = 0
    if(sign_bit == '1'):
        extend = '1111111111111111'
    if(sign_bit == '0'):
        extend = '0000000000000000'
    
    output = extend + value
    return output


def main_loop(file, instructions):

    # inicializando variáveis
    clock_cycle = 0
    pc = 0 # Program Counter
    arquivo = open("report.txt", "w", encoding='utf-8') # Arquivo para Salvar dados

    #Instanciando Memória de Instruções de acordo com o tipo de entrada
    inst_memory = instructions_memory.Instruction_Memory()
    if(file == 0):
        inst_memory.store_in_memory_instruction(0, instructions)
    else:
        inst_memory.store_in_memory_instruction(file, 0)

    main_control = control.Main_Control() # Instanciando controle principal
    register_base = registerBase.Register_Base() # Instanciando Banco de Registradores
    alucontrol = ALUControl.ALUControl() # Instanciando controle da ALU
    alu = ALU.ALU()
    data_memory = dataMemory.Data_Memory() # Instanciando Memória de Dados


    # Loop Principal do pipeline
    instructions_count = inst_memory.get_instruction_memory_length()
    count = 0
    while count < instructions_count:
        print('\n')

        # ---------------------------------------------- Instruction Fetch / IF -------------------------------------------------------

        instruction = inst_memory.get_instruction(pc)
        clock_cycle += 1

        print('Ciclo de Clock: ', clock_cycle)
        print("PC: ", functions.int_binary_conversion(pc))
        print("Instrução: ", instruction)

        arquivo.write("Ciclo de Clock: ")
        arquivo.write(str(clock_cycle))
        arquivo.write('\n')
        arquivo.write("Program Counter: ")
        arquivo.write(functions.int_binary_conversion(pc))
        arquivo.write('\n')
        arquivo.write("Instrução: ")
        arquivo.write(instruction)
        arquivo.write('\n')
        pc += 4
        # ---------------------------------------------- Instruction Decode / ID -------------------------------------------------------

        fields = functions.divider(instruction) # Divide a instrução de acordo com o tipo de instrução
        control_signs = main_control.get_output(fields['op']) # Gerando sinais de controle

        sign_extended = 0 # Extensão de Sinal
        
        muxReg = fields['rd'] if control_signs['RegDist'] == 1 else fields['rt'] # Multiplexador para definir registrador de escrita
        registerOutput = register_base.get_output(fields['rs'], fields['rt'], muxReg, 0, control_signs['RegWrite'], 0) # Entrada do Ranco de Registradores

        if(fields['address'] != -1):
            sign_extended = sign_extend(fields['address'])

        alucontrol.set_opalu(fields['funct'], control_signs['ALUOp']) # Gerando sinal da ALU
        output_alucontrol = alucontrol.get_op()

        # ---------------------------------------------- Execution / EXE ----------------------------------------------------------
        muxAlu = registerOutput['readData2'] if control_signs['ALUSrc'] == 0 else sign_extended # Multiplexador para definir origem da ALU
        alu_output = alu.get_output(output_alucontrol, registerOutput['readData1'], muxAlu)

        # Realiza Salto
        if control_signs['Branch'] == 1:
            if alu.get_zero() == 1:
                jump = functions.instruction_int_conversion(fields['address'])
                pc = pc + jump
        else:
            # ---------------------------------------------- Memory Access / MEM -------------------------------------------------------
            data_memory_output = -1
            if(control_signs['MemWrite'] == 1 or control_signs['MemRead'] == 1):
                data_memory_output = data_memory.get_output(alu_output, registerOutput['readData2'], control_signs['MemWrite'], control_signs['MemRead'])
            # ---------------------------------------------- Escrita / WB --------------------------------------------------------------

            if(control_signs['Branch'] == 0 and control_signs['RegWrite'] == 1):
                # muxWb = data_memory_output if control_signs['MemtoReg'] == 1 else alu_output
                muxWb = alu_output
                registerOutput = register_base.get_output(fields['rs'], fields['rt'], muxReg, muxWb, control_signs['RegWrite'], 1) # Escrevendo no Banco de Registradores
            
            # ---------------------------------------------------------------------------------------------------------------------------

        print("Banco de Registradores")
        arquivo.write("Sinais de Controle:")
        arquivo.write('ALUOp :')
        arquivo.write(control_signs['ALUOp'])
        arquivo.write('\n')

        arquivo.write("Banco de Registradores:")
        arquivo.write('\n')
        registers_write = register_base.get_register_base()
        for position in registers_write:
            arquivo.write(position.getAssemblyCode())
            arquivo.write(': ')
            arquivo.write(position.getValue())
            arquivo.write('\n')

        arquivo.write("Memória de Dados:")
        arquivo.write('\n')
        data_memory_write = data_memory.get_data_memory()
        for position in data_memory_write:
            arquivo.write(position)
            arquivo.write('\n')
        
        arquivo.write('\n')
        

        register_base.show_register_base()
        count = count + 1 # Incrementando Loop
    print("\nPipeline Finalizado")