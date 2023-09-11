import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year did you want to travel to? Type tha date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/2012-09-22/"
SPOTIPY_CLIENT_ID = '6370f5b911ed4c8690e614178aaf1027'
SPOTIPY_CLIENT_SECRET = 'ae102c78809947899baaf9e22c0aa817'

response = requests.get(URL)
html_web = response.text

soup = BeautifulSoup(html_web, 'html.parser')
soup_names_spans = soup.select('li ul li h3')
song_titles = [song.text.strip() for song in soup_names_spans]
song_titles = song_titles

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
                        scope="playlist-modify-private",
                        redirect_uri="http://example.com",
                        client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        show_dialog=True,
                        cache_path="token.txt",
                        username='Md.Balaka', ))
user_id = spotify.current_user()["id"]
playlist_name = f'Tracks from {date}!'
playlist_description = f'The most popular tracks from {date} date.'
new_playlist = spotify.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)
playlist_id = new_playlist['id']

songs_uris = []
year = date.split('-')[0]
for song in song_titles:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

spotify.playlist_add_items(playlist_id=playlist_id, items=songs_uris)


