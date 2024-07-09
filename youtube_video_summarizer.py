import os
import openai
import json
import re
from time import time, sleep
from urllib.parse import urlparse, parse_qs
import textwrap
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter



def get_transcript(url):
    url_data = urlparse(url)
    video_id = parse_qs(url_data.query)["v"][0]
    if not video_id:
        print('Video ID not found.')
        return None

    try:
        formatter = TextFormatter()

        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        text = formatter.format_transcript(transcript)
        text = re.sub('\s+', ' ', text).replace('--', '')
        return video_id, text

    except Exception as e:
        print('Error downloading transcript:', e)
        return None