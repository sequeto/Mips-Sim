import functions

class ALU:
    def __init__(self):
        self.aluop = -1
        self.zero = -1
        self.result = -1
    

    def get_output(self, ALUoperation, ReadData1, ReadData2):
        value1 = functions.instruction_int_conversion(ReadData1)
        value2 = functions.instruction_int_conversion(ReadData2)

        if(ALUoperation == "0000"):
            count = 0
            binary_data1 = functions.int_binary_conversion(ReadData1)
            binary_data2 = functions.int_binary_conversion(ReadData2)
            result_aux = ''
            while count < 32:
                if binary_data1[count] == 1 and binary_data2[count] == 1:
                    result_aux = result_aux + 1
                else:
                    result_aux = result_aux + 0
                count = count + 1
            
            self.result = result_aux
                
        elif(ALUoperation == "0001"):
            count = 0
            binary_data1 = functions.int_binary_conversion(ReadData1)
            binary_data2 = functions.int_binary_conversion(ReadData2)
            result_aux = ''
            while count < 32:
                if binary_data1[count] == 1 or binary_data2[count] == 1:
                    result_aux = result_aux + 1
                else:
                    result_aux = result_aux + 0
                count = count + 1
            
            self.result = result_aux

        elif(ALUoperation == "0010"):
            self.result = value1 + value2

        elif(ALUoperation == "0110"):
            self.result = value1 - value2

        elif(ALUoperation == "0111"):
            if value1 < value2:
                self.result = 1
            else:
                self.result = 0

        elif(ALUoperation == "1100"):
            pass

        if self.result == 0:
            self.zero = 1
        else:
            self.zero = 0

        self.result = functions.int_binary_conversion(self.result)

        return self.result
        

        def get_zero(self):
            return self.zero