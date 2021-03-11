
import os
import google_auth_oauthlib.flow #google authentication library
import googleapiclient.discovery
import googleapiclient.errors
import google_auth_oauthlib.flow
import connect_to_spotify


def get_youtube_client():
    """Youtube Data API """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()

    # Youtube DATA API
    youtube_client = googleapiclient.discovery.build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        credentials=credentials)

    return youtube_client



def take_playlist_videos(youtube_playlist_name):
    youtube_client = get_youtube_client()
    request = youtube_client.playlists().list(
            part="snippet, id",
            mine= 'true',
            maxResults = 50
        )
    response = request.execute()
    print(f"Total number of playlists on youtube account: {len(response['items'])} (Note: The max that youtube API allows us to see is 50)")

    for playlist in response['items']:
        if playlist['snippet']['title'] == youtube_playlist_name:
            print(f"Name of youtube playlist that we will create in spotify: {youtube_playlist_name}")
            playlist_id = playlist['id']
        #print(playlist['snippet']['title'])

    #get details from the specific playlist using playlist Id
    request = youtube_client.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=2,
        playlistId = playlist_id
    )
    response = request.execute() #response is a dictionary

    all_song_info = {}
    for item in response['items']:
        video_title = item['snippet']['title']
        youtube_url = f"https://www.youtube.com/watch?v={item['id']}"
        artist = video_title.split("-")[0]
        song_title = video_title.split("-")[1].split("(")[0]
        all_song_info[video_title] = {
            "youtube_url": youtube_url,
            "artist": artist,
            "song_title": song_title,
            "spotify_uri": connect_to_spotify.get_spotify_uri(song_title, artist)

        }
    return all_song_info


if __name__ == "__main__":
    artists, song_titles = take_playlist_videos()

