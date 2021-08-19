# Converte a instrução em inteiro 
def instruction_int_conversion(string_instruction):
    int_value = int(string_instruction, 2)
    return int_value

# Converte o inteiro em binário de 32 bits
def int_binary_conversion(int_value):
    binary_value = '{:032b}'.format(int_value)
    return binary_value

# Lê um arquivo passado para a função
def read_file(file_name):
    file = open(file_name)
    lines = file.readlines()
    return lines


def divider(binary_instruction):
    fields = {
        'type': -1,
        "op" : -1,
        "rs" : -1,
        "rt" : -1,
        "rd" : -1,
        "shamt" : -1,
        "funct" : -1,
        "address" : -1,
    }

    fields['op'] = binary_instruction[0:6] # 31:26
    fields['rs'] = binary_instruction[6:11] # 25:21
    fields['rt'] = binary_instruction[11:16] # 20:16

    # R-Type (0)
    if fields['op'] == '000000':
        fields['type'] = "R"
        fields['rd'] = binary_instruction[16:21] # 15:11
        fields['shamt'] = binary_instruction[21:26] # 10:6
        fields['funct'] = binary_instruction[26:32] # 5:0

    #load or store (35 or 45) or Branch (4)
    if fields['op'] == '100011' or fields['op'] == '101101' or fields['op'] == '000100':
        fields['address'] = binary_instruction[16:32] # 15:0
        if fields['op'] == '100011':
            fields['type'] = "load"
        elif fields['op'] == '101101':
            fields['type'] = "store"
        elif fields['op'] == '000100':
            fields['type'] = "branch"

    return fields