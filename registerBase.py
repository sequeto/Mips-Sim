import register
import functions

class Register_Base:
    def __init__(self):
        self.RegWrite = -1
        self.registerBase = []
    
        self.registerBase.append(register.Register("00000", "0", "$zero"))
        self.registerBase.append(register.Register("00001", "1", "$at"))

        self.registerBase.append(register.Register("00010", "2", "$v0"))
        self.registerBase.append(register.Register("00011", "3", "$v1"))

        self.registerBase.append(register.Register("00100", "4", "$a0"))
        self.registerBase.append(register.Register("00101", "5", "$a1"))
        self.registerBase.append(register.Register("00110", "6", "$a2"))
        self.registerBase.append(register.Register("00111", "7", "$a3"))

        self.registerBase.append(register.Register("01000", "8", "$t0"))
        self.registerBase.append(register.Register("01001", "9", "$t1"))
        self.registerBase.append(register.Register("01010", "10", "$t2"))
        self.registerBase.append(register.Register("01011", "11", "$t3"))
        self.registerBase.append(register.Register("01100", "12", "$t4"))
        self.registerBase.append(register.Register("01101", "13", "$t5"))
        self.registerBase.append(register.Register("01110", "14", "$t6"))
        self.registerBase.append(register.Register("01111", "15", "$t7"))

        self.registerBase.append(register.Register("10000", "16", "$s0"))
        self.registerBase.append(register.Register("10001", "17", "$s1"))
        self.registerBase.append(register.Register("10010", "18", "$s2"))
        self.registerBase.append(register.Register("10011", "19", "$s3"))
        self.registerBase.append(register.Register("10100", "20", "$s4"))
        self.registerBase.append(register.Register("10101", "21", "$s5"))
        self.registerBase.append(register.Register("10110", "22", "$s6"))
        self.registerBase.append(register.Register("10111", "23", "$s7"))

        self.registerBase.append(register.Register("11000", "24", "$t8"))
        self.registerBase.append(register.Register("11001", "25", "$t9"))

        self.registerBase.append(register.Register("11010", "26", "$k0"))
        self.registerBase.append(register.Register("11011", "27", "$k1"))

        self.registerBase.append(register.Register("11100", "28", "$gp"))

        self.registerBase.append(register.Register("11101", "29", "$k1"))

        self.registerBase.append(register.Register("11110", "30", "$k1"))

        self.registerBase.append(register.Register("11111", "31", "$k1"))

    # Realiza Escrita do registrador
    def writeRegister(self, index, value):
        register = self.registerBase[index]
        register.setValue(value)
        print("Valor Escrito:", register.getValue())


    def get_output(self, register1, register2, writeRegister, writeData, RegWrite, clock):

        # converter binario dos registros
        index1 = functions.instruction_int_conversion(register1)
        index2 = functions.instruction_int_conversion(register2)
        index3 = functions.instruction_int_conversion(writeRegister)

        if(RegWrite == 1 and clock == 1):
            self.writeRegister(index3, writeData)
        
        # Cria saída
        output = {
            "readData1":-1,
            "readData2":-1
        }
        output['readData1'] = self.registerBase[index1].getValue()
        output['readData2'] = self.registerBase[index2].getValue()

        return output

