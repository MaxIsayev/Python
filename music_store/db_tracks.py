import sqlite3
from typing import Any
import PySimpleGUI as sg

def create_tracks(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS tracks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(200),
length TIME,
bitrate INTEGER,
year_released INTEGER,
genre VARCHAR(200),
track_rating INTEGER,
album_id INTEGER REFERENCES albums(id)
);
'''
    cursor.execute(query)
    connector.commit()

def get_tracks(connection: sqlite3.Connection, cursor: sqlite3.Cursor)-> list[Any]:
    query = "SELECT * FROM tracks"
    with connection:
        try:
            cursor.execute(query)
            tracks = cursor.fetchall()
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")
            return []
    return tracks

def insert_track(connection: sqlite3.Connection, 
                    cursor: sqlite3.Cursor,
                    name, 
                    length, 
                    bitrate, 
                    year_released, 
                    genre, 
                    track_rating, 
                    album_id
                    ):
    query = '''
            INSERT INTO tracks (name, length, bitrate, year_released, genre, track_rating, album_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
    with connection:
        try:
            cursor.execute(query, (name, length, bitrate, year_released, genre, track_rating, album_id))
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")    

def delete_track(connector: sqlite3.Connection, cursor: sqlite3.Cursor, id):   
    query = "DELETE FROM tracks WHERE id=?"        
    with connector:
        try:
            cursor.execute(query, (id,))
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")    
    
def update_track(connector: sqlite3.Connection, 
                    cursor: sqlite3.Cursor,
                    name, 
                    length, 
                    bitrate, 
                    year_released, 
                    genre, 
                    track_rating, 
                    album_id,
                    id):        
    with connector:
        try:
            cursor.execute(''' UPDATE tracks
                                SET name = ? ,
                                length = ? , 
                                bitrate = ? ,
                                year_released = ? , 
                                genre = ? ,
                                track_rating = ? ,     
                                album_id = ?                                 
                              WHERE id = ?''', (name, length, bitrate, year_released, genre, track_rating, album_id, id))  
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")        