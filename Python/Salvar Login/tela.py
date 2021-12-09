from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('SystemDefault') # tema da tela
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,0))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(21,1))],
    [sg.Checkbox('Salvar o loguin?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Leitura de Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'paulovrn12@gmail.com' and valores['senha'] == 'Editor@w123':
            print('Bem Vindo!')

