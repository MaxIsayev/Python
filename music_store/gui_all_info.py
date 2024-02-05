import PySimpleGUI as sg
from db_all_info import *

def open_all_info(main_window: sg.Window):  
    main_window.hide()

    connector = sqlite3.connect('music_store.db')
    cursor = connector.cursor()

    layout = [ 
        [sg.Table(get_all_info(connector, cursor), 
                  key="-TABLE-", expand_x=True,
                  headings=("N", "Name", "Length", "Bitrate", "Year released", "Genre", "Track rating", 
                            "Album name", "Album year","Album number of songs", "Album rating",
                            "Musician name", "Musician nickname", "Musician date of birth"))],       
        [   
            sg.Input(key="-COLUMNFILTER-", size=20, default_text="column name to filter"),
            sg.Input(key="-VALUEFILTER-", size=20, default_text="filter value"),         
            sg.Button("Filter", key="-FILTER-")            
        ], 
        [   
            sg.Input(key="-COLUMNSORT-", size=20, default_text="column name to sort"),
            sg.Button("Sort ascending", key="-ASCSORT-"),            
            sg.Button("Sort descending", key="-DESCSORT-")
        ], 
        [            
            sg.Button("Return", key="-RETURN-"),
            sg.Button("Reset table", key="-RESET-")
        ]          
    ]

    window = sg.Window("All tracks general info | Music store database PTU20", layout, element_padding=10, resizable=True)

    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break  
        if event == "-FILTER-":
            window["-TABLE-"].update(values=get_filtered_info(connector, cursor, values["-COLUMNFILTER-"], values["-VALUEFILTER-"]))
        if event == "-RESET-": 
            window["-TABLE-"].update(values=get_all_info(connector, cursor))    
        if event == "-ASCSORT-":
            window["-TABLE-"].update(values=get_sorted_info(connector, cursor, values["-COLUMNSORT-"], "ASC"))
        if event == "-DESCSORT-":
            window["-TABLE-"].update(values=get_sorted_info(connector, cursor, values["-COLUMNSORT-"], "DESC"))

    window.close()
    main_window.un_hide()
    connector.close()