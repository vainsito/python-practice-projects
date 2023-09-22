import PySimpleGUI as sg

# Theme of the Calculator
def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = ('Arial', 16), button_element_size = (6, 3), element_padding = (2, 2))
    button_size = (6, 3)
    # Layout of the Calculator
    layout = [
        [sg.Text(
            '', 
            key = '-OUTPUT-', 
            pad = (10,20), 
            justification = 'rigth', 
            expand_x=True, font=('Arial', 24),
            right_click_menu=theme_menu)
         ],
        [sg.Button('Clear', key = '-CLEAR-', expand_x = True), sg.Button('Enter', key = '-ENTER-', expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('/', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.',  size = button_size), sg.Button('+', size = button_size)]
    ]
    return sg.Window('Calculator', layout)
theme_menu = ['menu', ['Material2', 'dark', 'LightGray1', 'random']]
window = create_window('Material2')

current_numb = [] # List to store the current number
operation = [] # List to store the operation

# Loop to keep the window open
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()  # close the window 
        window = create_window(event) # create and open the new window

    if event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
        current_numb.append(event)
        numb_string = ''.join(current_numb)
        window['-OUTPUT-'].update(numb_string)
        
    if event in ['+', '-', '*', '/']:
        if current_numb:
            operation.append(''.join(current_numb)) # Add the current number to the list
            current_numb = [] # Clear the current number
            operation.append(event) # Add the operation to the list
            window['-OUTPUT-'].update('') # Clear the output
        
    if event == '-ENTER-':
        if current_numb and operation:
            operation.append(''.join(current_numb)) # Add the current number to the list
            result = eval(''.join(operation)) # Evaluate the operation
            window['-OUTPUT-'].update(result) # Update the output
            current_numb = [str(result)] # Set the current number to the result
            operation = [] # Clear the operation
        else:
            window['-OUTPUT-'].update('Error: no operations') # Display an error message if there is no operation to evaluate
        
    if event == '-CLEAR-':
        current_numb = []
        operation = []
        window['-OUTPUT-'].update('')

    
window.close()