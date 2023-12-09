import os
import google.auth
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json
keys_json = 'keys.json'
with open(keys_json) as keys_data:
    keys = json.load(keys_data)

api_key = keys['youtube_api_key']
channel_id = keys["channel_id"]

def get_playlist_id(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the uploads playlist ID for the given channel ID
    response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return uploads_playlist_id


