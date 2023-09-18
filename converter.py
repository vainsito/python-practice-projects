import PySimpleGUI as sg

# Define the first element

# In layout you can define the elements that you want to show in the window,
# Each list inside the list is a row in the window
layout = [
    [sg.Text('Text'), sg.Spin(['Item 1', 'Item 2'])], # We can Add Key to the elements to identify them
    [sg.Button('Ok', key = '-BUTTON1-')], # Conventionally the keys are in capital letters and preceded and followed by an underscore 
    [sg.Input()],
    [sg.Text('Hello'), sg.Button('Exit', key = '-BUTTON2-')]
]

# This function take two arguments, the first is the tittle of the window and the second is the layout of the window
window = sg.Window('Converter', layout) # With method read() the window is shown

# This loop is to keep the window open, and read the events

while True:
    event, values = window.read() # This method return two values, the first is the event and the second is the values of the window
    
    if event == sg.WIN_CLOSED: # If the user closes the window
        break
    # We define the events with the name of the buttons
    if event == 'Button1':
        print('Button Ok was pressed')
    if event == 'Button2':
        print('Button Exit was pressed')
        break
window.close()