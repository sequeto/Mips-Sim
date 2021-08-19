import functions

class ALUControl:
    def __init__(self):
        self.op: -1
        self.tablecode = {
            "0000":'and',
            "0001":'or',
            "0010":'add',
            "0110":'subtract',
            "0111":'set on less than',
            "1100":'nor',
        }

    def set_opalu(self, funct, ALUop):
        if(ALUop == '00'):
            self.op = "0010"

        if(ALUop == '01'):
            self.op = "0110"

        if(ALUop == '10'):
            formatted_funct = funct[2:6]
            if(formatted_funct == "0010"):
                self.op = "0110"

            elif(formatted_funct == "0000"):
                self.op = "0010"
            
            elif(formatted_funct == "0100"):
                self.op = "0000"
            
            elif(formatted_funct == "0101"):
                self.op = "0001"
            
            elif(formatted_funct == "1010"):
                self.op = "0111"
            
    def get_op(self):
        return self.op
    
    def get_op_table(self, op):
        return self.table[op]