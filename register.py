class Register:
    def __init__(self, binaryCode, decimalCode, assemblyCode):
        self.binaryCode = binaryCode
        self.decimalCode = decimalCode
        self.assemblyCode = assemblyCode
        self.value = -1
    
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value
    
    def getDecimalCode(self):
        return self.decimalCode

    def getBinaryCode(self):
        return self.binaryCode

    def getAssemblyCode(self):
        return self.assemblyCode