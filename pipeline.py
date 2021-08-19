import functions
import instructions_memory
import registerBase
import control
import ALUControl
import dataMemory
import ALU


def main_loop(file, instructions):

    # inicializando variáveis
    clock_cycle = 0
    pc = 0 # Program Counter

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
    # data_memory = dataMemory.Data_Memory() # Instanciando Memória de Dados


    # Loop Principal do pipeline
    instructions_count = inst_memory.get_instruction_memory_length()
    count = 0
    while count < instructions_count:
        print('\n')

        # ---------------------------------------------- Instruction Fetch / IF -------------------------------------------------------
        instruction = inst_memory.get_instruction(pc)
        clock_cycle += 1 
        print("PC: ", pc)
        print("Instrução: ", instruction)
        pc += 4

        # ---------------------------------------------- Instruction Decode / ID -------------------------------------------------------
        fields = functions.divider(instruction) # Divide a instrução de acordo com o tipo de instrução
        control_signs = main_control.get_output(fields['op']) # Gerando sinais de controle
        
        muxReg = fields['rd'] if control_signs['RegDist'] == 1 else fields['rt'] # Multiplexador para definir registrador de escrita
        registerOutput = register_base.get_output(fields['rs'], fields['rt'], muxReg, 0, control_signs['RegWrite'], 0) # Entrada do Ranco de Registradores

        alucontrol.set_opalu(fields['funct'], control_signs['ALUOp']) # Gerando sinal da ALU
        output_alucontrol = alucontrol.get_op()

        # ---------------------------------------------- Execution / EXE -------------------------------------------------------
        muxAlu = registerOutput['readData2'] if control_signs['ALUSrc'] == 0 else 0 # Multiplexador para definir origem da ALU (colocar Sinal extendido do Address)
        alu_output = alu.get_output(output_alucontrol, registerOutput['readData1'], muxAlu)

        # ---------------------------------------------- Memory Access / MEM -------------------------------------------------------

        




        count = count + 1 # Incrementando Loop