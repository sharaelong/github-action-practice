import os
from googleapiclient.discovery import build

youtube_api_key = os.environ['YOUTUBE_API_KEY']

youtube = build('youtube', 'v3', developerKey=youtube_api_key)
request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
response = request.execute()
print(response)
