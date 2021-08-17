class Instruction_Memory:
    def __init__(self):
        self.instruction_memory = []
        self.pc = 0

    # Converte a instrução em inteiro 
    def instruction_int_conversion(self,string_instruction):
        int_value = int(string_instruction, 2)
        return int_value

    # Lê um arquivo passado para a função
    def read_file(self,file_name):
        file = open(file_name)
        lines = file.readlines()
        return lines

    # Realiza leitura do arquivo ou recebe manualmente e guarda as instruções convertidas em inteiro na memória de instruções
    def store_in_memory_instruction(self, file_name, instructions):
        counter = 0
        binary_instructions = 0

        if file_name == 0:
            binary_instructions = instructions
        else:
            binary_instructions = self.read_file(file_name)

        for instruction in binary_instructions:
            if counter > 127:
                print("Memória de Instruções Cheia")
                break
            else:
                int_instruction = self.instruction_int_conversion(instruction)
                self.instruction_memory.append(int_instruction)
                counter = counter + 1

        
    # mostra a memoria de instruções
    def show_instruction_memory(self):
        print(self.instruction_memory)
    
    # mostra a memoria de instruções
    def read_instruction_memory(self):
        for instruction in self.instruction_memory:
            print("PC: ", self.pc *4)
            print("Instrução:", instruction)
            self.pc += 1
    
    def get_instruction(self, index):
        return self.Instruction_Memory[index]
    
    def get_pc(self):
        return self.pc
    
    def get_instruction_memory_length(self):
        return len(self.instruction_memory)


# # Lê um arquivo dado como parâmetro
# def read_param_file(self):
#     file_name = sys.argv[1]
#     file = open(file_name)
#     lines = file.readlines()
#     return lines