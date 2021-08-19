import functions
import instructions_memory
import registerBase


def main_loop(file, instructions):

    # inicializando variáveis
    clock_cycle = 0
    pc = 0

    #Inicializando Memória de Instruções de acordo com o tipo de entrada
    inst_memory = instructions_memory.Instruction_Memory()
    if(file == 0):
        inst_memory.store_in_memory_instruction(0, instructions)
    else:
        inst_memory.store_in_memory_instruction(file, 0)

    
    instructions_count = inst_memory.get_instruction_memory_length()

    # Loop Principal do pipeline
    count = 0
    while count < instructions_count:

        # ---------------------------------------------- Instruction Fetch / IF -------------------------------------------------------
        instruction = inst_memory.get_instruction(pc)
        clock_cycle += 1 
        print("PC: ", pc)
        print("Instrução: ", instruction)
        pc += 4

        # ---------------------------------------------- Instruction Decode / ID -------------------------------------------------------
        # Dividir a instrução de acordo com o tipo de instrução
        fields = functions.divider(instruction)



        count = count + 1 # Incrementando Loop