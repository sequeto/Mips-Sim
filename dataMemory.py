import functions

class Data_Memory:
    def __init__(self):
        self.data_memory = []
        count  = 0

        # Inicializando memória de dados (128 posições de 32 bits (4 Bytes) - 512 Bytes)
        while count < 128:
            self.data_memory.append('00000000000000000000000000000000')
            count = count + 1
        self.MemWrite = -1
        self.MemRead = -1
        self.output = -1
    
    def reset(self):
        count  = 0
        while count < 128:
            self.data_memory.append('00000000000000000000000000000000')
            count = count + 1

    def get_output(self, address, WriteData, MemWrite, MemRead):
        index = functions.instruction_int_conversion(address)
        if MemWrite == 1:
            self.data_memory[index] = WriteData
            self.output = 0
        
        if MemRead == 1:
            self.output = self.data_memory[index]
        
        return self.output
    
    def show_data_memory(self):
        print(self.data_memory)
    
    def get_data_memory(self):
        return self.data_memory
        