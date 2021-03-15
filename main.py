"""
To do in this project:

step 1: log into youtube
step 3: open up spotify and log in
step 4: create new playlist in spotify
step 4: copy name of artist and song in youtube playlist into spotify playlist
"""

import get_youtube_videos
import connect_to_spotify

def make_spotify_playlist(youtube_playlist_name, new_playlist_name):

    #connect to youtube and get name of artist and song into dictionary
    all_info = get_youtube_videos.take_playlist_videos(youtube_playlist_name = youtube_playlist_name)

    #get spotify uri from song info dictionary
    uris = [all_info[item]['spotify_uri'] for item in all_info.keys()]

    #create playlist
    playlist_id = connect_to_spotify.request_to_spotify(new_playlist_name = new_playlist_name )

    #add songs to playlist
    connect_to_spotify.add_song_to_playlist(playlist_id, uris)

if __name__ == "__main__":
    make_spotify_playlist(youtube_playlist_name = "for spotify", new_playlist_name = "new playlist!")





