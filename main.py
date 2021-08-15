import sys

# Converte a instrução em inteiro 
def instruction_int_conversion(string_instruction):
    int_value = int(string_instruction, 2)
    print(int_value)
    return int_value

# Converte o inteiro em binário de 32 bits
def int_binary_conversion(int_value):
    binary_value = '{:032b}'.format(int_value)
    # binary_value = bin(int_value)
    print(binary_value)
    # print(type(binary_value))
    return binary_value

# Lê um arquivo dado como parâmetro
def read_param_file():
    file_name = sys.argv[1]
    file = open(file_name)
    lines = file.readlines()
    # for line in lines:
    #     print(line)
    return lines

# Realiza leitura do arquivo e guarda as instruções convertidas em inteiro na memória de instruções
def store_in_memory_instruction():
    counter = 0
    memory_instruction = []
    binary_instructions = read_param_file()
    for instruction in binary_instructions:
        if counter > 1:
            print("Memória de Instruções Cheia")
            break
        else:
            int_instruction = instruction_int_conversion(instruction)
            memory_instruction.append(int_instruction)
            counter = counter + 1

    print(memory_instruction)
    return memory_instruction

def interface():
    print("Selecione uma das opções: ")
    print("Carga do Arquivo: ")
    print("Entrada via Teclado: ")
    print("Início da Execução: ")
    print("Reset: ")






# Ambito de Testes (Todas as funções comentadas para teste rápido)
# store_in_memory_instruction()
# read_param_file()
# instruction_int_conversion("00000000000000000000000000000000")
int_binary_conversion(5)