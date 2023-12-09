import os
import google.auth
from googleapiclient.discovery import build
import json


def get_video_list(channel_id, api_key, output_file):
    print("fetching latest videos")
    youtube = build('youtube', 'v3', developerKey=api_key)
    next_page_token = None
    total_results = []
    while True:
        playlist_items = youtube.playlistItems().list(
            part='snippet',
            maxResults=50,
            playlistId=channel_id,
            pageToken = next_page_token
        ).execute()
        filtered_items = []
        for item in playlist_items.get('items', []):
            snippet = item.get('snippet', {})
            resourceId = snippet.get('resourceId', {})
            filtered_item = {
                'title': snippet.get('title'),
                'publishedAt': snippet.get('publishedAt'),
                'videoId': resourceId.get('videoId'),
            }
            filtered_items.append(filtered_item)
        total_results.extend(filtered_items)
        
        next_page_token = playlist_items.get('nextPageToken')
        if not next_page_token:
            break
    with open(output_file, 'w') as json_file:
        json.dump(total_results, json_file, indent=2)
    print(f'video metadata has been downloaded to {output_file}')
