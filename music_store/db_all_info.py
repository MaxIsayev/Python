import sqlite3
import PySimpleGUI as sg
from typing import Any

query = '''
    SELECT tracks.id, tracks.name, tracks.length, tracks.bitrate, tracks.year_released, tracks.genre, tracks.track_rating, 
        albums.name, albums.year_released, albums.number_of_songs, albums.album_rating,
        musicians.name,  musicians.nickname,  musicians.date_of_birth
    FROM tracks
    JOIN albums ON tracks.album_id = albums.id
    JOIN musicians ON musicians.id = albums.musician_id
'''

def get_all_info(connection: sqlite3.Connection, cursor: sqlite3.Cursor)-> list[Any]:
    with connection:
        try:
            cursor.execute(query)
            info = cursor.fetchall()
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")
            return []
    return info

def get_column_by_name(column_heading: str)->str:  
    if column_heading.lower() in ["n", "id"]:
        return "tracks.id"
    elif column_heading.lower() == "name":
        return "tracks.name"
    elif column_heading.lower() == "length":
        return "tracks.length"
    elif column_heading.lower() == "bitrate":
        return "tracks.bitrate"
    elif column_heading.lower() == "year released":
        return "tracks.year_released"
    elif column_heading.lower() == "genre":
        return "tracks.genre"
    elif column_heading.lower() == "track rating":
        return "tracks.track_rating"
    elif column_heading.lower() == "album name":
        return "albums.name"
    elif column_heading.lower() == "album year":
        return "albums.year_released"
    elif column_heading.lower() == "album number of songs":
        return "albums.number_of_songs"
    elif column_heading.lower() == "album rating":
        return "albums.album_rating"
    elif column_heading.lower() == "musician name":
        return "musicians.name"
    elif column_heading.lower() == "musician nickname":
        return "musicians.nickname"
    elif column_heading.lower() == "musician date of birth":
        return "musicians.date_of_birth"   
    else:
        return column_heading

def get_filtered_info(connection: sqlite3.Connection, cursor: sqlite3.Cursor, column_to_filter, value)-> list[Any]:
    with connection:
        filter_query = f"{query}\n WHERE {get_column_by_name(column_to_filter)} = ?"
        try:
            cursor.execute(filter_query, (value,))
            filtered_info = cursor.fetchall()
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")
            return []
    return filtered_info 
    
def get_sorted_info(connection: sqlite3.Connection, cursor: sqlite3.Cursor, column_to_sort, order_type)-> list[Any]:
    with connection: 
        sort_query = f"{query}\n ORDER BY {get_column_by_name(column_to_sort)} {order_type}"
        try:
            cursor.execute(sort_query)
            ordered_info = cursor.fetchall()
        except Exception as error:
            sg.PopupOK(f"DB Error {error.__class__.__name__}: {error}", title="DB Error")
            return []
    return ordered_info 
    
