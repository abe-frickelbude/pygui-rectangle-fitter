import PySimpleGUI as sg  # Part 1 - The import
from PySimpleGUI.PySimpleGUI import _DebugWin

sg.theme('dark grey 4')

input_column = [
    [sg.Text('Source rectangle')],
    [sg.Push(), sg.Text("Width"), sg.Input(key='sw', enable_events=True)],
    [sg.Push(), sg.Text("Height"), sg.Input(key='sh', enable_events=True)],
    [sg.HorizontalSeparator()],
    [sg.Text('Target rectangle')],
    [sg.Push(), sg.Text("Width"), sg.Input(key='tw', enable_events=True)],
    [sg.Push(), sg.Text("Height"), sg.Input(key='th', enable_events=True)],
    [sg.HorizontalSeparator()],
    [sg.Button('Quit')]
]

canvas_column = [
    [sg.Graph(canvas_size=(1034, 586), graph_bottom_left=(5, 5), graph_top_right=(1024, 576),
              background_color='white', key='canvas')],
]

layout = [
    [sg.Column(input_column), sg.VSeparator(), sg.Column(canvas_column)]
]

# sg.theme_previewer()

# Create the window
mainWindow = sg.Window('Rectangle fit').Layout(layout).finalize()

# Reroute sdtout to debug window
debug = sg.Print(size=(70, 20), relative_location=(200, 200),
                 #no_button=True,
                 do_not_reroute_stdout=False
                 )

debugWindow = _DebugWin.debug_window

mainWindow.move(300, 0)

#debugWindow.move(400,300)

# event loop
while True:
    event, values = mainWindow.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    #print(values)

mainWindow.close()
