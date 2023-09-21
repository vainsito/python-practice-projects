import PySimpleGUI as sg

# Theme of the Calculator
def create_window(theme):
    sg.theme('theme')
    sg.set_options(font = ('Arial', 16), button_element_size = (6, 3), element_padding = (2, 2))
    button_size = (6, 3)
    # Layout of the Calculator
    layout = [
        [sg.Text('ouput', key = '-OUTPUT-', pad = (10,20), justification = 'rigth', expand_x=True, font=('Arial', 24))],
        [sg.Button('Clear', key = '-CLEAR-', expand_x = True), sg.Button('Enter', key = '-ENTER-', expand_x = True)],
        [sg.Button('7', key = '-7-', size = button_size), sg.Button('8', key = '-8-', size = button_size), sg.Button('9', key = '-9-', size = button_size), sg.Button('/', key = '-DIVIDE-', size = button_size)],
        [sg.Button('4', key = '-4-', size = button_size), sg.Button('5', key = '-5-', size = button_size), sg.Button('6', key = '-6-', size = button_size), sg.Button('*', key = '-MULTIPLY-', size = button_size)],
        [sg.Button('1', key = '-1-', size = button_size), sg.Button('2', key = '-2-', size = button_size), sg.Button('3', key = '-3-', size = button_size), sg.Button('-', key = '-SUBTRACT-', size = button_size)],
        [sg.Button('0', key = '-0-', expand_x = True), sg.Button('.', key = '-DOT-', size = button_size), sg.Button('+', key = '-ADD-', size = button_size)]
    ]
    return sg.Window('Calculator', layout)
theme_menu =
window = create_window('Material2')

# Loop to keep the window open
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()