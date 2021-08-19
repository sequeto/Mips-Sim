import functions

class Main_Control:
    def __init__(self):
        self.control_signs = {
            'RegDist': -1,
            'ALUSrc': -1,
            'MemtoReg': -1,
            'RegWrite': -1,
            'MemRead': -1,
            'MemWrite': -1,
            'Branch': -1,
            'ALUOp': -1
        }
    
    def get_output(self, opcode):
        if opcode == '000000':
            self.control_signs['RegDist'] = 1
            self.control_signs['ALUSrc'] = 0
            self.control_signs['MemtoReg'] = 0
            self.control_signs['RegWrite'] = 1
            self.control_signs['MemRead'] = 0
            self.control_signs['MemWrite'] = 0
            self.control_signs['Branch'] = 0
            self.control_signs['ALUOp'] = '10'
        elif opcode == '100011':
            self.control_signs['RegDist'] = 0
            self.control_signs['ALUSrc'] = 1
            self.control_signs['MemtoReg'] = 1
            self.control_signs['RegWrite'] = 1
            self.control_signs['MemRead'] = 1
            self.control_signs['MemWrite'] = 0
            self.control_signs['Branch'] = 0
            self.control_signs['ALUOp'] = '00'
        elif opcode == '101101':
            self.control_signs['RegDist'] = -1
            self.control_signs['ALUSrc'] = 1
            self.control_signs['MemtoReg'] = -1
            self.control_signs['RegWrite'] = 0
            self.control_signs['MemRead'] = 0
            self.control_signs['MemWrite'] = 1
            self.control_signs['Branch'] = 0
            self.control_signs['ALUOp'] = '00'
        elif opcode == '000100':
            self.control_signs['RegDist'] = -1
            self.control_signs['ALUSrc'] = 0
            self.control_signs['MemtoReg'] = -1
            self.control_signs['RegWrite'] = 0
            self.control_signs['MemRead'] = 0
            self.control_signs['MemWrite'] = 0
            self.control_signs['Branch'] = 1
            self.control_signs['ALUOp'] = '01'

        return self.control_signs

        