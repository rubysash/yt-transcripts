import tkinter as tk
from tkinter import scrolledtext
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
import datetime

def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.netloc == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.netloc in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        elif parsed_url.path.startswith('/embed/') or parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
    return None

def format_timestamp(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))  # e.g., 0:02:13

def fetch_transcript(event=None):
    url = url_entry.get().strip()
    video_id = extract_video_id(url)
    if not video_id:
        transcript_textbox.delete('1.0', tk.END)
        transcript_textbox.insert(tk.END, "Invalid YouTube URL format.")
        return
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatted = ""
        for entry in transcript:
            timestamp = format_timestamp(entry['start'])
            formatted += f"[{timestamp}] {entry['text']}\n"
        transcript_textbox.delete('1.0', tk.END)
        transcript_textbox.insert(tk.END, formatted)
    except Exception as e:
        transcript_textbox.delete('1.0', tk.END)
        transcript_textbox.insert(tk.END, f"Error: {str(e)}")

# Initialize GUI
root = tk.Tk()
root.title("YouTube Transcript with Timestamps")

# URL Entry
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(padx=10, pady=(10, 0), anchor="w")

url_entry = tk.Entry(root, width=100)
url_entry.pack(padx=10, pady=5, fill="x")
url_entry.bind("<Return>", fetch_transcript)
url_entry.bind("<FocusOut>", fetch_transcript)

# Transcript Display
transcript_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=30)
transcript_textbox.pack(padx=10, pady=(5, 10), fill="both", expand=True)

# Start GUI loop
root.mainloop()
