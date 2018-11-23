import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bottle import route, run, get, default_app, response
import random
import json
import api
PORT_NUMBER = 8890
SPOTIPY_CLIENT_ID = api.get_public_key()
SPOTIPY_CLIENT_SECRET = api.get_private_key()
client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@route('/', method="GET")
def start():
	print("Got a request!")
	results = sp.user_playlist("21pjjh7lp7b64noigouwmszea", api.get_playlist_id(), fields="tracks, next")
	i = 0
	end = False
	all_tracks = []
	while not end:
		while(i < len(results['tracks']['items'])):
			track = results['tracks']['items'][i]
			track_name = track['track']['name']
			all_tracks.append(track_name)
			i = i + 1
		if results['tracks']['next']:
			results = sp.next(results['tracks'])
			i = 0
		else:
			end = True
	result_track = random.choice(all_tracks)
	response.headers['Cache-Control'] = 'no-cache'
	return result_track

if __name__ == '__main__':
	run(server='flup', host='localhost', port=PORT_NUMBER)
else:
	app = application = default_app()

