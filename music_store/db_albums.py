import sqlite3
from typing import Any
import PySimpleGUI as sg

def create_albums(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS albums (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(200),
year_released INTEGER,
number_of_songs INTEGER,
album_rating INTEGER,
musician_id INTEGER REFERENCES musicians(id)
);
'''
    cursor.execute(query)
    connector.commit()

def get_albums(connection: sqlite3.Connection, cursor: sqlite3.Cursor)-> list[Any]:
    query = "SELECT * FROM albums"
    with connection:
        try:
            cursor.execute(query)
            albums = cursor.fetchall()
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")
            return []
    return albums

def insert_album(connection: sqlite3.Connection, 
                    cursor: sqlite3.Cursor,
                    name, 
                    year_released, 
                    number_of_songs, 
                    album_rating, 
                    musician_id
                    ):
    query = "INSERT INTO albums (name, year_released, number_of_songs, album_rating, musician_id) VALUES (?, ?, ?, ?, ?)"
    with connection:
        try:
            cursor.execute(query, (name, year_released, number_of_songs, album_rating, musician_id))
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")    

def delete_album(connector: sqlite3.Connection, cursor: sqlite3.Cursor, id):   
    query = "DELETE FROM albums WHERE id=?"        
    with connector:
        try:
            cursor.execute(query, (id,))
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")    
    
def update_album(connector: sqlite3.Connection, 
                    cursor: sqlite3.Cursor,
                    name, 
                    year_released, 
                    number_of_songs, 
                    album_rating, 
                    musician_id,
                    id):        
    with connector:
        try:
            cursor.execute(''' UPDATE albums
                                SET name = ? ,
                                year_released = ? , 
                                number_of_songs = ? ,
                                album_rating = ? ,   
                                musician_id = ?                                 
                              WHERE id = ?''', (name, year_released, number_of_songs, album_rating, musician_id, id))  
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")        