import logging

import PySimpleGUI as sg

import Rectangle as rc


def init_gui(viewport_size: (int, int)):
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
        [sg.Graph(canvas_size=viewport_size, graph_bottom_left=(0, 0), graph_top_right=viewport_size,
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


def draw_source_rect(rect: rc.Rectangle, graph: sg.Graph):
    x1 = rect.x + rect.width
    y1 = rect.y + rect.height
    graph.DrawRectangle((rect.x, rect.y), (x1, y1), line_color='blue', line_width=2)


def draw_target_rect(rect: rc.Rectangle, graph: sg.Graph):
    x1 = rect.x + rect.width
    y1 = rect.y + rect.height
    graph.DrawRectangle((rect.x, rect.y), (x1, y1), line_color='red', line_width=2)


def calculate_best_fit(source_rect: rc.Rectangle, target_rect: rc.Rectangle):
    ##
    if target_rect.aspect_ratio() < source_rect.aspect_ratio():
        scale_factor = source_rect.height / target_rect.height
    else:
        scale_factor = source_rect.width / target_rect.width

    out_width = round(scale_factor * target_rect.width)
    out_height = round(scale_factor * target_rect.height)

    out_x = round(0.5 * (source_rect.width - out_width)) + source_rect.x  # don't forget the source origin
    out_y = round(0.5 * (source_rect.height - out_height)) + source_rect.y

    return rc.Rectangle(out_x, out_y, out_width, out_height)


def fit_to_viewport(rect: rc.Rectangle, viewport_size: (float, float), max_scale: float):
    ##
    viewport_aspect_ratio = viewport_size[0] / viewport_size[1]

    if rect.aspect_ratio() < viewport_aspect_ratio:
        scale_factor = viewport_size[1] / rect.height
    else:
        scale_factor = viewport_size[0] / rect.width

    out_width = round(max_scale * scale_factor * rect.width)
    out_height = round(max_scale * scale_factor * rect.height)

    out_x = round(0.5 * (viewport_size[0] - out_width))
    out_y = round(0.5 * (viewport_size[1] - out_height))

    return rc.Rectangle(out_x, out_y, out_width, out_height)


def main():
    #
    VIEWPORT_SIZE = (500, 500)
    MAX_SCALE = 0.9

    main_window, graph = init_gui(VIEWPORT_SIZE)

    # event loop
    while True:
        try:
            event, values = main_window.read()

            # listen for 'quit'
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break

            dimensions = read_inputs(values)
            source_rect = rc.Rectangle(0.0, 0.0, dimensions['source_width'], dimensions['source_height'])
            target_rect = rc.Rectangle(0.0, 0.0, dimensions['target_width'], dimensions['target_height'])

            graph.erase()

            if source_rect.is_defined() and target_rect.is_defined():
                # for display (both rectangles fitted into the viewport)
                fitted_source_rect = fit_to_viewport(source_rect, VIEWPORT_SIZE, MAX_SCALE)
                draw_source_rect(fitted_source_rect, graph)
                draw_target_rect(calculate_best_fit(fitted_source_rect, target_rect), graph)

                # for outputting the actual dimensions
                best_fit_rect = calculate_best_fit(source_rect, target_rect)
                print(best_fit_rect)

        except Exception as ex:
            logging.exception(ex)

    main_window.close()


main()
