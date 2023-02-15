import PySimpleGUI as sg
import pyautogui
import time

# Define o layout da janela
layout = [
    [sg.Column([[sg.Text('Navegador'), sg.Input(key='campo1')], 
                [sg.Text('Contato'), sg.Input(key='campo2')], 
                [sg.Text('Mensagem'), sg.Input(key='campo3')], 
                [sg.Text('Quantidade'), sg.Input(key='campo4')]], 
               element_justification='c')],
    [sg.Button('Enviar')]
]

# Cria a janela
window = sg.Window('Bot de Mensagens', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        # Recupera os valores digitados e os salva em variáveis separadas
        nav = values['campo1']
        cont = values['campo2']
        msg = values['campo3']
        quant = values['campo4']
        # Fecha a janela
        window.close()
        break


pyautogui.press("win")
time.sleep(1.3)
pyautogui.write(nav)
time.sleep(1.3)
pyautogui.press("enter")
time.sleep(4)

# localizar o alvo desejado
pyautogui.write("web.whatsapp.com")
pyautogui.press("Enter")
time.sleep(5)

# localizar o contato escolhido
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(cont)
time.sleep(1.3)
pyautogui.press('enter')

# digitar a mensagem

formatado = int(quant)

for num in range(formatado):
    pyautogui.write(msg)
    pyautogui.press('enter')

msg1 = 'Obrigado por usar nosso sistema!'

# Define o layout da janela
layout2 = [
    [sg.Text(msg1, font=('Helvetica', 20), text_color='white', background_color='blue', 
             size=(40, 3), justification='center', key='-TEXT-')],
    [sg.Button('Fechar', size=(10, 2), pad=(130, 20), button_color=('white', 'red'))]
]

# Cria a janela
janela = sg.Window('Aviso', layout2, background_color='', alpha_channel=1, 
                   no_titlebar=True, grab_anywhere=True, keep_on_top=True)

# Define a velocidade da animação
velocidade = 5

# Inicia a animação
while True:
    evento, valores = janela.read(timeout=velocidade)
    if evento == sg.WIN_CLOSED or evento == 'Fechar':
        break
    # Move a mensagem para a esquerda
    janela['-TEXT-'].update(pyautogui.scroll(-1, 5))

# Fecha a janela
janela.close()