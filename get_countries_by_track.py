import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your own client_id and client_secret
client_id = '21c2c79dc3cf407b9a6f6f1ff9b7485b'
client_secret = input("client_secret_id: ")

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_available_countries(track_uri):
    try:
        # Get track details
        track = sp.track(track_uri)

        # Get availability information
        available_markets = track.get("available_markets", [])

        
        return available_markets

    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    # I Feel Love - Donna Summer
    track_uri = 'spotify:track:7B7lf3sIze5VR2WuYttn18'  # Replace with the URI of the track you want to check
    countries = get_available_countries(track_uri)
    
    if countries:
        print(f"The track is available in the following countries:")
        print(countries)
    else:
        print("No information available for this track.")