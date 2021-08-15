import PySimpleGUI as sg

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
            output = values['-ENTER-']
        except:
            output = 'Invalid'

        window['-OUTPUT-'].update(output)
    else:
        break