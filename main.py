import sys
import register
import instructions_memory

def initialize_registers():
    registerBase = []
    
    registerBase.append(register.Register("00000", "0", "$zero"))
    registerBase.append(register.Register("00001", "1", "$at"))

    registerBase.append(register.Register("00010", "2", "$v0"))
    registerBase.append(register.Register("00011", "3", "$v1"))

    registerBase.append(register.Register("00100", "4", "$a0"))
    registerBase.append(register.Register("00101", "5", "$a1"))
    registerBase.append(register.Register("00110", "6", "$a2"))
    registerBase.append(register.Register("00111", "7", "$a3"))

    registerBase.append(register.Register("01000", "8", "$t0"))
    registerBase.append(register.Register("01001", "9", "$t1"))
    registerBase.append(register.Register("01010", "10", "$t2"))
    registerBase.append(register.Register("01011", "11", "$t3"))
    registerBase.append(register.Register("01100", "12", "$t4"))
    registerBase.append(register.Register("01101", "13", "$t5"))
    registerBase.append(register.Register("01110", "14", "$t6"))
    registerBase.append(register.Register("01111", "15", "$t7"))

    registerBase.append(register.Register("10000", "16", "$s0"))
    registerBase.append(register.Register("10001", "17", "$s1"))
    registerBase.append(register.Register("10010", "18", "$s2"))
    registerBase.append(register.Register("10011", "19", "$s3"))
    registerBase.append(register.Register("10100", "20", "$s4"))
    registerBase.append(register.Register("10101", "21", "$s5"))
    registerBase.append(register.Register("10110", "22", "$s6"))
    registerBase.append(register.Register("10111", "23", "$s7"))

    registerBase.append(register.Register("11000", "24", "$t8"))
    registerBase.append(register.Register("11001", "25", "$t9"))

    registerBase.append(register.Register("11010", "26", "$k0"))
    registerBase.append(register.Register("11011", "27", "$k1"))

    registerBase.append(register.Register("11100", "28", "$gp"))

    registerBase.append(register.Register("11101", "29", "$k1"))

    registerBase.append(register.Register("11110", "30", "$k1"))

    registerBase.append(register.Register("11111", "31", "$k1"))



    # zero = register.Register("00000", "0", "$zero")
    # at = register.Register("00001", "1", "$at")

    # v0 = register.Register("00010", "2", "$v0")
    # v1 = register.Register("00011", "3", "$v1")

    # a0 = register.Register("00100", "4", "$a0")
    # a1 = register.Register("00101", "5", "$a1")
    # a2 = register.Register("00110", "6", "$a2")
    # a3 = register.Register("00111", "7", "$a3")

    # t0 = register.Register("01000", "8", "$t0")
    # t1 = register.Register("01001", "9", "$t1")
    # t2 = register.Register("01010", "10", "$t2")
    # t3 = register.Register("01011", "11", "$t3")
    # t4 = register.Register("01100", "12", "$t4")
    # t5 = register.Register("01101", "13", "$t5")
    # t6 = register.Register("01110", "14", "$t6")
    # t7 = register.Register("01111", "15", "$t7")

    # s0 = register.Register("10000", "16", "$s0")
    # s1 = register.Register("10001", "17", "$s1")
    # s2 = register.Register("10010", "18", "$s2")
    # s3 = register.Register("10011", "19", "$s3")
    # s4 = register.Register("10100", "20", "$s4")
    # s5 = register.Register("10101", "21", "$s5")
    # s6 = register.Register("10110", "22", "$s6")
    # s7 = register.Register("10111", "23", "$s7")

    # t8 = register.Register("11000", "24", "$t8")
    # t9 = register.Register("11001", "25", "$t9")

    # k0 = register.Register("11010", "26", "$k0")
    # k1 = register.Register("11011", "27", "$k1")

    # gp = register.Register("11100", "28", "$gp")

    # sp = register.Register("11101", "29", "$k1")

    # fp = register.Register("11110", "30", "$k1")

    # ra = register.Register("11111", "31", "$k1")

    print (registerBase[0].getValue())

# Ambito de Testes (Todas as funções comentadas para teste rápido)

# initialize_registers()