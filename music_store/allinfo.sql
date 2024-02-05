-- SQLite
--headings=("N", "Name", "Length", "Bitrate", "Year released", "Genre", "Track rating", 
--                            "Album mane", "Album year","Album number of songs", "Album rating",
--                            "Musician name", "Musician nickname", "Musician date of birth"))],  
SELECT tracks.id, tracks.name, tracks.length, tracks.bitrate, tracks.year_released, tracks.genre, tracks.track_rating, 
        albums.name, albums.year_released, albums.number_of_songs, albums.album_rating,
        musicians.name,  musicians.nickname,  musicians.date_of_birth
FROM tracks
JOIN albums ON tracks.album_id = albums.id
JOIN musicians ON musicians.id = albums.musician_id