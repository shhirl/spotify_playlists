
import json
import requests


# get my access tokens
with open('spotify_secret.json') as json_file:
    data = json.load(json_file)
    user_id = data['spotify']['user_id']
    spotify_token = data['spotify']['spotify_token']


def request_to_spotify(new_playlist_name):
    # make a request to make a playlist
    request_body = json.dumps({
        "name" : new_playlist_name,
        "description" : "Songs",
        "public": True
    })

    #query to create playlist
    query = f"https://api.spotify.com/v1/users/{user_id}/playlists"

    response = requests.post(
        query,
        data=request_body,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_token}"
        }
    )

    print(f"reponse for creating new spotify playlist: {response}")
    response_json = response.json()

    #get the playlist id of the new playlist you created
    return response_json["id"]




def get_spotify_uri(song_title, artist):
    """
    spotify URI is a resource identifier that allows you to locate an artist, album or track
    """

    #query to search for the song
    query = f"https://api.spotify.com/v1/search?query=track%3A{song_title}+artist%3A{artist}&type=track&offset=0&limit=20"
    response = requests.get(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_token}"
        }
    )


    response_json = response.json()

    songs = response_json["tracks"]["items"]

    #only get uri from first song
    uri = songs[0]["uri"]
    return uri



def add_song_to_playlist(playlist_id, uris):
    #add all songs into new playlist using uris
    request_data = json.dumps(uris)

    #query to add song to playlist
    query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    response = requests.post(
        query,
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    print(f"reponse for adding songs to spotify playlist: {response}")

