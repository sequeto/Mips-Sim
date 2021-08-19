import functions

class Instruction_Memory:
    def __init__(self):
        self.instruction_memory = []

    def get_instruction(self, index):
        return self.instruction_memory[int(index/4)]

    # Realiza leitura do arquivo ou recebe manualmente e guarda as instruções convertidas em inteiro na memória de instruções
    def store_in_memory_instruction(self, file_name, instructions):
        counter = 0
        binary_instructions = 0

        if file_name == 0:
            binary_instructions = instructions
        else:
            binary_instructions = functions.read_file(file_name)

        for instruction in binary_instructions:
            if counter > 127:
                print("Memória de Instruções Cheia")
                break
            else:
                self.instruction_memory.append(instruction)
                counter = counter + 1
        
    # mostra a memoria de instruções
    def show_instruction_memory(self):
        print(self.instruction_memory)
    
    # mostra a memoria de instruções
    def read_instruction_memory(self):
        for instruction in self.instruction_memory:
            print("Instrução:", instruction)
    
    def get_instruction_memory_length(self):
        return len(self.instruction_memory)
        
        
        


# # Lê um arquivo dado como parâmetro
# def read_param_file(self):
#     file_name = sys.argv[1]
#     file = open(file_name)
#     lines = file.readlines()
#     return lines