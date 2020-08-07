import spotipy
import spotipy.util as util


CLIENT_ID = 
CLIENT_SECRET = 

token = util.oauth2.SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)

sp.user_playlist_tracks()
