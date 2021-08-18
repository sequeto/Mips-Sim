import functions

class main_control:
    def __init__(self):
        self.control_signs = {
            'Branch': -1,
            'MemRead': -1,
            'MemtoReg': -1,
            'ALUOp': -1,
            'MemWrite': -1,
            'ALUSrc': -1,
            'RegWrite': -1
        }
    
    def get_output(self, input):
        pass