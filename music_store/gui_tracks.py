import PySimpleGUI as sg
from db_tracks import *

def open_tracks(main_window: sg.Window):  
    main_window.hide()

    connector = sqlite3.connect('music_store.db')
    cursor = connector.cursor()
    create_tracks(connector, cursor) 

    layout = [ 
        [sg.Table(get_tracks(connector, cursor), 
                  key="-TABLE-", expand_x=True,
                  headings=("N", "Name", "Length", "Bitrate", "Year released", "Genre", "Track rating", "Album id"))],
        [   
            [
                sg.Input(key="-NAMEINSERT-", size=20, default_text="Name to insert"),
                sg.Input(key="-LENGTHINSERT-", size=20, default_text="Length to insert"),
                sg.Input(key="-BITRATEINSERT-", size=20, default_text="Bitrate to insert"),  
                sg.Input(key="-YEARRELEASEDINSERT-", size=20, default_text="Year released to insert"),
            ],
            [
                sg.Input(key="-GENREINSERT-", size=20, default_text="Genre to insert"),
                sg.Input(key="-TRACKRATINGINSERT-", size=20, default_text="Track rating to insert"),  
                sg.Input(key="-ALBUMIDINSERT-", size=20, default_text="Album id insert"),  
            ],                     
            sg.Button("Insert row", key="-INSERT-")            
        ],               
        [   
            [
                sg.Input(key="-IDUPDATE-", size=20, default_text="id to update"),
                sg.Input(key="-NAMEUPDATE-", size=20, default_text="new name"),
                sg.Input(key="-LENGTHUPDATE-", size=20, default_text="new length"),
                sg.Input(key="-BITRATEUPDATE-", size=20, default_text="new bitrate"),  
            ],
            [
                sg.Input(key="-YEARRELEASEDUPDATE-", size=20, default_text="new year released"),
                sg.Input(key="-GENREUPDATE-", size=20, default_text="new genre"),
                sg.Input(key="-TRACKRATINGUPDATE-", size=20, default_text="new track rating"),   
                sg.Input(key="-ALBUMIDUPDATE-", size=20, default_text="new album id") 
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

    window = sg.Window("Tracks | Music store database PTU20", layout, element_padding=10, resizable=True)

    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break    
        if event == "-INSERT-":
            insert_track(connector, cursor, 
                         values["-NAMEINSERT-"], values["-LENGTHINSERT-"], values["-BITRATEINSERT-"], values["-YEARRELEASEDINSERT-"],
                         values["-GENREINSERT-"], values["-TRACKRATINGINSERT-"], values["-ALBUMIDINSERT-"])             
        if event == "-DELETE-":
            delete_track(connector, cursor, values["-IDDELETE-"])
        if event == "-UPDATE-":
            update_track(connector, cursor, 
                         values["-NAMEUPDATE-"], values["-LENGTHUPDATE-"], values["-BITRATEUPDATE-"], values["-YEARRELEASEDUPDATE-"],
                         values["-GENREUPDATE-"], values["-TRACKRATINGUPDATE-"], values["-ALBUMIDUPDATE-"], values["-IDUPDATE-"])   
        window["-TABLE-"].update(values=get_tracks(connector, cursor))     
    window.close()
    main_window.un_hide()
    connector.close()