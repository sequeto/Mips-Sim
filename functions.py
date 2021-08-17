# Converte a instrução em inteiro 
def instruction_int_conversion(string_instruction):
    int_value = int(string_instruction, 2)
    return int_value

# Converte o inteiro em binário de 32 bits
def int_binary_conversion(int_value):
    binary_value = '{:032b}'.format(int_value)
    return binary_value