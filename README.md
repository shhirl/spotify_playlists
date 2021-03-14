# Automatically Generate Spotify Playlist from Youtube Playlist
This Python program automates the creation of a personal Spotify playlist directly from a personal Youtube playlist.   

## Requirements
- Pyenv installed to create a virtual environment
- A Google account
- A Spotify account


## How to run
To automate your own Spotify playlist creation, please follow the following instructions:

1. Clone this repo
2. Install dependencies with the command `pip install -r requirements.txt`
3. Get your Youtube credentials 
4. Create a file named `client_secret.json` and put your Youtube credentials inside
5. Get your spotify OAuth Token here: https://developer.spotify.com/console/post-playlists/  
    - Log into Spotify Developer portal
    - Go to the 'Post Playlist' Page
    - Fill in your Spotify user ID and click "Get Token"
    <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/spotify_token.jpg" width="500">
7. Create a file named `spotify_secret.json` and put your Spotify credentials inside
8. Edit the file `main.py` to include the name of your Youtube playlist, and the name of the Spotify playlist that will be created
9. Run the program with the command `python main.py`
10. Google will ask your permission to access their API. Click through and 
11. When the code runs, you will see your new playlist appear in Spotify!


## Info on Youtube and Spotify Credentials
* Youtube API Overview: https://developers.google.com/youtube/v3/getting-started
* Instructions on google apis here: https://github.com/googleapis/google-api-python-client.  
* For google_auth_oauthlib.flow: https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html


