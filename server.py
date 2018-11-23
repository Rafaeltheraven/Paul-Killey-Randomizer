import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bottle import route, run, get, default_app, response
import random
import json
PORT_NUMBER = 8890
SPOTIPY_CLIENT_ID = '1966863ffee1447487dd26e031db4d64'
SPOTIPY_CLIENT_SECRET = "e68f42eff93b4d19905cf30dc1496d97"
client_credentials_manager = SpotifyClientCredentials("1300bfed2ce24c1b887a352c1b79af89", "c465a9558e1f4f2bb7ad3ae4208aeee6")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@route('/', method="GET")
def start():
	print("Got a request!")
	results = sp.user_playlist("21pjjh7lp7b64noigouwmszea", "2KP4hhopN5IaNKexMlyCBR", fields="tracks, next")
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

