import functions

class Data_Memory:
    def __init__(self):
        self.data_memory = []
        count  = 0

        # Inicializando memória de dados (128 posições de 32 bits (4 Bytes) - 512 Bytes)
        while count < 127:
            self.data_memory.append('00000000000000000000000000000000')
            count = count + 1
        self.MemWrite = -1
        self.MemRead = -1
        self.output = -1

    def get_output(self, address, WriteData, MemWrite, MemRead):
        if MemWrite == 1:
            self.data_memory[address] = WriteData
            self.output = 0
        
        if MemRead == 1:
            self.output = self.data_memory[address]
        
        return self.output
        