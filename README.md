# Automatically Generate Spotify Playlist from Youtube Playlist
This Python program automates the creation of a personal Spotify playlist directly from a personal Youtube playlist.  

# Try it for yourself!
## Requirements
- Pyenv installed to create a virtual environment
- A Google account
- A Spotify account


## How to run
To automate your own Spotify playlist creation, please follow the following instructions:

1. Clone this repo

2. Install dependencies with the command `pip install -r requirements.txt`

3. Get your Youtube credentials 
    - Create a new project on your Google Developer Console and give the project a name. You will need to create an account and log in if you don't already have one https://console.cloud.google.com/ 
    
      <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/create_project_google_developer.jpg" width="500">
    
    - Navigate to GoogleAPIs here https://console.cloud.google.com/apis/library?project=tester-api-keyenable. Scroll down to the Youtube Data API v3 and click one it. Then click enable
    
      <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/youtube_api1.jpg" width="500">
    
      <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/youtube_api2" width="500">
    
    - Open the Credentials page in the API Console
    
    - Generate OAuth 2.0 credentials
    
4. Create a file named `client_secret.json` and put your Youtube credentials inside

    - The three credentials that you need to fill in are "client_id", "client_secret" and "api_key". The other fields should be same as in this image

      <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/client_secret_json_example.jpg" width="500">

5. Get your spotify OAuth Token here: https://developer.spotify.com/console/post-playlists/  
    - Log into Spotify Developer portal
    - Go to the 'Post Playlist' Page
    - Fill in your Spotify user ID and click "Get Token"
    <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/spotify_token.jpg" width="500">

6. Create a file named `spotify_secret.json` and put your Spotify credentials inside

    - The json should follow the same format as in the image below. The two credentials that you need to fill in are "user_id" and "spotify_token"
    - <img src="https://github.com/shhirl/spotify_playlists/blob/main/images/spotify_secret_json_example.jpg" width="500">

7. Edit the file `main.py` to include the name of your Youtube playlist, and the name of the Spotify playlist that will be created

8. Run the program with the command `python main.py`

9. Google will ask your permission to access their API. Click through and 

10. When the code runs, you will see your new playlist appear in Spotify!


## Info on Youtube and Spotify Credentials
* Youtube API Overview: https://developers.google.com/youtube/v3/getting-started
* Instructions on google apis here: https://github.com/googleapis/google-api-python-client.  
* For google_auth_oauthlib.flow: https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html.  
* https://developer.spotify.com/documentation/general/guides/authorization-guide/


# Example
The Youtube playlist that I have created looks like this:   
<img src="https://github.com/shhirl/spotify_playlists/blob/main/images/youtube_playlist.jpg" width="700">


After running this Python script, I will see a new Spotify playlist that looks like this   
<img src="https://github.com/shhirl/spotify_playlists/blob/main/images/final_result.jpg" width="900">
