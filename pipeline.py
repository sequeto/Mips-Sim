import functions
import instructions_memory
import registerBase
import control
import ALUControl
import dataMemory


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
    # alucontrol = ALUControl.ALUControl() # Instanciando controle da ALU
    # register_base = registerBase.Register_Base() # Instanciando Banco de Registradores
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
        print(fields)
        control_signs = main_control.get_output(fields['op']) # Passa o Campo OP para o Controle Principal
        print(control_signs)




        count = count + 1 # Incrementando Loop