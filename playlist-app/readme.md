## Playlist-app

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `createdb playlist-app`
5. `flask run`

Flask Playlist Application
Overview
This Flask application allows users to upload songs and create custom playlists. The app uses WTForms for song and playlist submission and SQLAlchemy as the ORM for database interactions. Users can create playlists for different activities such as workouts, commuting, and falling asleep.

Features:
Upload songs with details such as title, artist, and genre.
Create custom playlists and add songs to them.
View and manage playlists.
Simple and intuitive user interface.
