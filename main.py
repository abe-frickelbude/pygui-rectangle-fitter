import logging

import PySimpleGUI as sg


def init_gui():
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
        [sg.Graph(canvas_size=(1044, 596), graph_bottom_left=(5, 5), graph_top_right=(1044, 596),
                  background_color='white', key='graph')],
    ]

    layout = [
        [sg.Column(input_column), sg.VSeparator(), sg.Column(canvas_column)]
    ]

    # sg.theme_previewer()

    # Reroute sdtout to debug window
    # Note: size() is in "terminal units", i.e. here 70 columns x 20 rows
    debug = sg.Print(size=(70, 20), location=(10, 10), do_not_reroute_stdout=False)

    # Create the window
    main_window = sg.Window('Rectangle fit').Layout(layout).finalize()

    # mainWindow.move(0, 0)  # to upper-left corner of the screen
    return main_window, main_window['graph']


def read_inputs(event_values):
    return {
        'source_width': int(event_values['sw']) if event_values['sw'] else 0,
        'source_height': int(event_values['sh']) if event_values['sh'] else 0,
        'target_width': int(event_values['tw']) if event_values['tw'] else 0,
        'target_height': int(event_values['th']) if event_values['th'] else 0
    }


def draw_source_rect(rect: (int, int, int, int), graph: sg.Graph):
    x1 = rect[0] + rect[2]
    y1 = rect[1] + rect[3]
    graph.DrawRectangle((rect[0], rect[1]), (x1, y1), line_color='blue', line_width=2)


def draw_target_rect(rect: (int, int, int, int), graph: sg.Graph):
    x1 = rect[0] + rect[2]
    y1 = rect[1] + rect[3]
    graph.DrawRectangle((rect[0], rect[1]), (x1, y1), line_color='red', line_width=2)


def main():
    main_window, graph = init_gui()
    # event loop
    while True:
        try:
            event, values = main_window.read()

            # listen for 'quit'
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break

            dimensions = read_inputs(values)
            # print(dimensions)

            graph.erase()
            draw_source_rect((10, 10, dimensions['source_width'], dimensions['source_height']), graph)
            draw_target_rect((10, 10, dimensions['target_width'], dimensions['target_height']), graph)

        except Exception as ex:
            logging.exception(ex)

    main_window.close()


main()
