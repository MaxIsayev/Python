#Main Window
import PySimpleGUI as sg
from gui_musicians import open_musicians
from gui_tracks import open_tracks
from gui_albums import open_albums
from gui_all_info import open_all_info

sg.set_options(font="comic-sans 12")
sg.theme("BrightColors")

main_layout = [
    [           
        sg.Button("Edit musicians", key="-MUSICIANS-", size=15),        
    ],
    [       
        sg.Button("Edit tracks", key="-TRACKS-", size=15),
    ],    
    [
        sg.Button("Edit albums", key="-ALBUMS-", size=15),
    ],
    [
        sg.Button("View all tracks general info", key="-INFO-", size=25),
    ],
    [
        sg.Button("Exit", key="-EXIT-", size=15),
    ],
]

main_window = sg.Window(
    "Music store database PTU20", 
    main_layout, 
    element_justification="center", 
    element_padding=10,    
    finalize=True,      
)

while True:   
    event, values = main_window.read(timeout=0.1) 
    if event in [sg.WINDOW_CLOSED, "-EXIT-"]:
        break
    if event == "-MUSICIANS-":
        open_musicians(main_window)
    if event == "-TRACKS-":
        open_tracks(main_window)
    if event == "-ALBUMS-":
        open_albums(main_window)
    if event == "-INFO-":
        open_all_info(main_window)
    
