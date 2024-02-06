import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#import pandas as pd

# Replace with your own client_id and client_secret
client_id = '21c2c79dc3cf407b9a6f6f1ff9b7485b'
client_secret = input("client secret id: ")

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_track_lengths(playlist_id):


    fields = "items.track.duration_ms" #get only time durations


    tracks = sp.playlist_items(playlist_id, fields=fields)
    
    times = []
    for i in tracks["items"]:
        times += [i["track"]["duration_ms"]]

    return times


if __name__ == "__main__":
    playlist_id = "2TwMeIdJNAE91mWKlt02ZJ"
    get_track_lengths(playlist_id)