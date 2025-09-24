import os
import base64
from dotenv import load_dotenv
from openai import OpenAI
import requests



# Load environment variables from .env file
load_dotenv()

class QwenAPI:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("qwen_key"),
            base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        )

    def upload_temp_mp3(self, path: str) -> str:
        print(f"Uploading {path} to catbox.moe")
        with open(path, "rb") as f:
            r = requests.post(
                "https://catbox.moe/user/api.php",
                data={"reqtype": "fileupload"},
                files={"fileToUpload": f}
            )
        return r.text.strip()

    def call_qwen(self, url: str) -> str:
        print(f"Calling qwen with url: {url}")
        completion = self.client.chat.completions.create(
            model="qwen3-omni-30b-a3b-captioner",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": url
                            }
                        }
                    ]
                }
            ]
        )
        return completion.choices[0].message.content, completion

import yt_dlp
import json
import os

class Data_Fetcher: 
    def __init__(self):
        self.songs = []
    
    def get_songs(self):
        with open("data/songs.json", "r") as f:
            self.songs = json.load(f)
        return self.songs

    def youtube_search_to_mp3(self, song_name: str, artist: str, id: int, output: str = None):
        if output is None:
            output = f'data/{id}'
        # Create a better search query with both song name and artist
        query = f"{song_name} {artist}"
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{query}"])
        return output
    
    def cut_song(self, mp3_path: str, start: int, end: int, output: str = None):
        if output is None:
            output = mp3_path  # Default to same file
        
        # If input and output are the same, use a temporary file
        if mp3_path == output:
            temp_output = f"{output}.temp.mp3"
            os.system(f"ffmpeg -y -i {mp3_path} -ss {start} -to {end} {temp_output}")
            os.replace(temp_output, output)  # Replace original with cut version
        else:
            os.system(f"ffmpeg -y -i {mp3_path} -ss {start} -to {end} {output}")
        return output



if __name__ == "__main__":
    qwen = QwenAPI()
    data_fetcher = Data_Fetcher()
    songs = data_fetcher.get_songs()
    for i in range(3):
        song = songs[i]
        print(f"Processing: {song['name']} by {song['artist']}")
        data_fetcher.youtube_search_to_mp3(song["name"], song["artist"], song["id"])
        data_fetcher.cut_song(f'data/{song["id"]}.mp3', 0, 40, f'data/{song["id"]}.mp3')
        print(f"Completed: {song['name']}")