import json
import requests

with open('../tokens.json') as json_file:
    data = json.load(json_file)
    CLIENT_ID = data['CLIENT_ID']
    CLIENT_SECRET = data['CLIENT_SECRET']

AUTH_URL = 'https://accounts.spotify.com/api/token'

#In order to access the various endpoints of the Spotify API, we need to pass an access token
#we need to POST a request with our client credentials and save the appropriate part of the response:
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

print(f"auth response: {auth_response}") # we want response [200]

# # convert the response to JSON
auth_response_data = auth_response.json()
#
# # save the access token
access_token = auth_response_data['access_token']


#the are a million spotify endoints to access different things e.g artist information, playlists,
#there are also spotify-generated audio analysis of songs like their key, time signature, or “danceability.”
#To access them we send a GET request to the API server
# with our access_token in the header.


# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
# actual GET request with proper header

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

#turn it into json to get a look
r = r.json()
print(f"some spotify endpoints for individual track {r}")
