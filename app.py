import re 
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API")

def create_transcript(videoid): 
    transcript = YouTubeTranscriptApi.get_transcript(videoid)
    data = ""
    for item in transcript:
        data += " " + item['text']
    return data

def get_videoId(youtube_link):
    pattern = r"(?<=v=)[^&]+"
    match = re.search(pattern, youtube_link)
    if match:
        return match.group()
    else:
        return -1

def summary_extraction(transcription):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. Summarize the following text into a clear, concise abstract. Focus on the main points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ],
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

def start():
    youtube_link = input("Enter the YouTube video link: ")
    videoid = get_videoId(youtube_link)
    if videoid == -1:
        print("Please enter a correct YouTube video link.")
        print("*")
        start()
    else:
        transcription = create_transcript(videoid)
        if len(transcription) > 0:
            print("*")
            print("Video Summary")
            print("*")
            print(summary_extraction(transcription))

start()
