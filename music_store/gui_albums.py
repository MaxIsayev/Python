import PySimpleGUI as sg
from db_albums import *

def open_albums(main_window: sg.Window):  
    main_window.hide()

    connector = sqlite3.connect('music_store.db')
    cursor = connector.cursor()
    create_albums(connector, cursor) 

    layout = [ 
        [sg.Table(get_albums(connector, cursor), 
                  key="-TABLE-", expand_x=True,
                  headings=("N", "Name", "Year released", "Number of songs", "Album rating", "Musician id"))],
        [   
            [
                sg.Input(key="-NAMEINSERT-", size=20, default_text="Name to insert"),                
                sg.Input(key="-YEARRELEASEDINSERT-", size=20, default_text="Year released to insert"),
                sg.Input(key="-NUMBEROFSONGSINSERT-", size=20, default_text="Number of songs to insert"),
                sg.Input(key="-ALBUMRATINGINSERT-", size=20, default_text="Album rating to insert"),  
            ],
            [
                sg.Input(key="-MUSICIANIDINSERT-", size=20, default_text="Musician id insert"),                
            ],                     
            sg.Button("Insert row", key="-INSERT-")            
        ],               
        [   
            [
                sg.Input(key="-IDUPDATE-", size=20, default_text="id to update"),
                sg.Input(key="-NAMEUPDATE-", size=20, default_text="new name"),
                sg.Input(key="-YEARRELEASEDUPDATE-", size=20, default_text="new year released"),                
                sg.Input(key="-NUMBEROFSONGSUPDATE-", size=20, default_text="new number of songs"),                
            ],
            [
                sg.Input(key="-ALBUMRATINGUPDATE-", size=20, default_text="new album rating"),  
                sg.Input(key="-MUSICIANIDUPDATE-", size=20, default_text="new musician id"),                
            ],
            sg.Button("Update row", key="-UPDATE-")
        ],               
        [     
            sg.Input(key="-IDDELETE-", size=20, default_text="row id to delete"),       
            sg.Button("Delete row", key="-DELETE-")
        ], 
        [            
            sg.Button("Return", key="-RETURN-")
        ]     
    ]

    window = sg.Window("Albums | Music store database PTU20", layout, element_padding=10, resizable=True)

    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break 
        if event == "-INSERT-":
            insert_album(connector, cursor, 
                         values["-NAMEINSERT-"], values["-YEARRELEASEDINSERT-"], values["-NUMBEROFSONGSINSERT-"],
                         values["-ALBUMRATINGINSERT-"], values["-MUSICIANIDINSERT-"])             
        if event == "-DELETE-":
            delete_album(connector, cursor, values["-IDDELETE-"])
        if event == "-UPDATE-":
            update_album(connector, cursor, 
                         values["-NAMEUPDATE-"], values["-YEARRELEASEDUPDATE-"], values["-NUMBEROFSONGSUPDATE-"], 
                         values["-ALBUMRATINGUPDATE-"], values["-MUSICIANIDUPDATE-"],values["-IDUPDATE-"])   
        window["-TABLE-"].update(values=get_albums(connector, cursor))     
    window.close()
    main_window.un_hide()
    connector.close()