# Automatically Generate Spotify Playlist from Youtube Playlist

* In this python project, I provide with the name of a private youtube playlist I have created
* The scripts use the Youtube and Python API to create a new spotify playlist on my account with the songs from the youtube playlist


## Tools used:
* Youtube API Overview: https://developers.google.com/youtube/v3/getting-started
* Instructions on google apis here: https://github.com/googleapis/google-api-python-client.  
  Notes:
  - make new prohject on google developer account and enable youtube Data API
  - install google API client

* for google_auth_oauthlib.flow: https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html

## How to run
* install dependencies `pip install -r requirements.txt`
* get credentials and tokens from spotify and youtube
* edit youtube playlist name and new spotify playlist name in `main.py`
* run main.py `python main.py`
