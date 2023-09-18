import PySimpleGUI as sg

# Define the first elementena

# In layout you can define the elements that you want to show in the window,
# Each list inside the list is a row in the window
layout = [
    [
        sg.Input( key = '-INPUT-'), 
        sg.Spin(['Km to Miles', 'kg to pound', 'Sec to min', 'Pts to Cm', 'mm to Cm'], key='-UNITS-'), 
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Result: ', key = '-OUTPUT-')] 
]

# This function take two arguments, the first is the tittle of the window and the second is the layout of the window
window = sg.Window('Converter', layout) # With method read() the window is shown

# This loop is to keep the window open, and read the events

while True:
    event, values = window.read() # This method return two values, the first is the event and the second is the values of the window
    
    if event == sg.WIN_CLOSED: # If the user closes the window
        break
    
    if event == '-CONVERT-':
        in_value = values['-INPUT-']
        if in_value.isnumeric():
            match values['-UNITS-']:
                case 'Km to Miles':
                    out_value = round(float(in_value) * 0.621371, 2)
                    out_string = f'{in_value} km = {out_value} miles'
                case 'kg to pound':
                    out_value = round(float(in_value) * 2.20462, 2)
                    out_string = f'{in_value} kg = {out_value} lb'
                case 'Sec to min':
                    out_value = round(float(in_value) / 60, 4)
                    out_string = f'{in_value} sec = {out_value} min'
                case 'Pts to Cm':
                    out_value = round(float(in_value) * 0.0352777777814035, 5)
                    out_string = f'{in_value} pts = {out_value} cm'
                case 'mm to Cm':
                    out_value = round(float(in_value) / 10, 5)
                    out_string = f'{in_value} mm = {out_value} cm'
            window['-OUTPUT-'].update(out_string)
        else:
            window['-OUTPUT-'].update('Invalid input, please enter a number')        
window.close()