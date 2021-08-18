import PySimpleGUI as sg

import functions
import instructions_memory
import registerBase


sg.theme('Reddit')

layout = [ 
    [sg.Text('Entrada: '), sg.InputCombo(('Arquivo', 'Via Teclado'), size=(20, 1), default_value = 'Arquivo', key='-ENTERTYPE-')],
    [sg.Text('Selecione Arquivo (Caso opção de entrada seja: Arquivo): ')], 
    [sg.InputText(key= '-FILE-'), sg.FileBrowse()],
    [sg.Text('Digite as Instruções (Caso opção de entrada seja: Via Teclado): ')], 
    [sg.Multiline(key= '-ENTER-')],
    [sg.Txt('Saída:')],
    [sg.Output(size=(73,20),key='-OUTPUT-')],
    [sg.Button('Execução Direta'), sg.Button('Execução Passo-a-Passo'), sg.Button('Sair')]
]

window = sg.Window('Simulador MIPS', layout)

while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED and event != "Sair":
        try:
            #Inicializações
            clock_cycle = 0
            pc = 0
            inst_memory = instructions_memory.Instruction_Memory()

            if event == "Execução Direta":
                if values['-ENTERTYPE-'] == "Arquivo":
                    file = values['-FILE-']
                    inst_memory.store_in_memory_instruction(file, 0)

                    instructions_count = inst_memory.get_instruction_memory_length()

                    # Loop Principal
                    count = 0
                    while count < 20:
                        instruction = inst_memory.get_instruction(pc)
                        print("PC: ", pc)
                        print("Instrução: ", instruction)
                        pc = pc + 4

                        count = count + 1


                
                if values['-ENTERTYPE-'] == "Via Teclado":
                    instructions = values["-ENTER-"].split()
                    inst_memory.store_in_memory_instruction(0, instructions)

        except:
            output = 'Invalid'

    else:
        break