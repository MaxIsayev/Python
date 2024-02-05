import PySimpleGUI as sg
import sqlite3
from db_musicians import *

def open_musicians(main_window: sg.Window):  
    main_window.hide()

    connector = sqlite3.connect('music_store.db')
    cursor = connector.cursor()

    create_musicians(connector, cursor)    

    layout = [ 
        [sg.Table(get_musicians(connector, cursor), 
                  key="-TABLE-", expand_x=True,
                  headings=("N", "Name", "Nickname", "Date of birth"))],
        [   
            sg.Input(key="-NAMEINSERT-", size=20, default_text="name to insert"),
            sg.Input(key="-NICKNAMEINSERT-", size=20, default_text="nickname to insert"),
            sg.Input(key="-DATEOFBIRTHINSERT-", size=20, default_text="date of birth to insert"),  
            sg.Button("Insert row", key="-INSERT-")            
        ],               
        [   
            sg.Input(key="-IDUPDATE-", size=20, default_text="id to update"),
            sg.Input(key="-NAMEUPDATE-", size=20, default_text="new name"),
            sg.Input(key="-NICKNAMEUPDATE-", size=20, default_text="new nickname"),
            sg.Input(key="-DATEOFBIRTHUPDATE-", size=20, default_text="new date of birth"),                                
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

    window = sg.Window("Musicians | Music store database PTU20", layout, element_padding=10, resizable=True)

    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break   
        if event == "-INSERT-":
            insert_musician(connector, cursor, values["-NAMEINSERT-"], values["-NICKNAMEINSERT-"], values["-DATEOFBIRTHINSERT-"])             
        if event == "-DELETE-":
            delete_musician(connector, cursor, values["-IDDELETE-"])
        if event == "-UPDATE-":
            update_musician(connector, cursor, values["-NAMEUPDATE-"], values["-NICKNAMEUPDATE-"], values["-DATEOFBIRTHUPDATE-"], values["-IDUPDATE-"])
        window["-TABLE-"].update(values=get_musicians(connector, cursor))    
    window.close()
    main_window.un_hide()
    connector.close()