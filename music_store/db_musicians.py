import sqlite3
from typing import Any
import PySimpleGUI as sg

def create_musicians(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS musicians (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(200),
nickname VARCHAR(200),
date_of_birth DATE
);
'''
    cursor.execute(query)
    connector.commit()

def get_musicians(connection: sqlite3.Connection, cursor: sqlite3.Cursor)-> list[Any]:
    query = "SELECT * FROM musicians"
    with connection:
        try:
            cursor.execute(query)
            musicians = cursor.fetchall()
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")
            return []
    return musicians

def insert_musician(connection: sqlite3.Connection, 
                    cursor: sqlite3.Cursor,
                    name, 
                    nickname, 
                    date_of_birth
                    ):
    query = "INSERT INTO musicians (name, nickname, date_of_birth) VALUES (?, ?, ?)"
    with connection:
        try:
            cursor.execute(query, (name, nickname, date_of_birth))
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")    

def delete_musician(connector: sqlite3.Connection, cursor: sqlite3.Cursor, id):   
    query = "DELETE FROM musicians WHERE id=?"        
    with connector:
        try:
            cursor.execute(query, (id,))
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")    
    
def update_musician(connector: sqlite3.Connection, 
                    cursor: sqlite3.Cursor,
                    name, 
                    nickname, 
                    date_of_birth,
                    id):        
    with connector:
        try:
            cursor.execute(''' UPDATE musicians
                                SET name = ? ,
                                nickname = ? ,    
                                date_of_birth = ?                                 
                              WHERE id = ?''', (name, nickname, date_of_birth, id)) 
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")        