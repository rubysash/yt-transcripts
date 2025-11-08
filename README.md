# YouTube Transcript Viewer with Timestamps

A simple Python GUI app to extract YouTube video transcripts and format them with timestamps.

It works great until YT decides to ban your IP.    It's fast, doesn't require actual transcribing as it just downloads the text.

See the "transcriber" repo for something that works better, on any file and on all sorts of urls.  It's much more reliable, though I liked this while it worked.

---

## Screenshot
![App Screenshot](./screenshot.png)
---

##  Installation on Windows using venv

1. **Create a virtual environment**  
```
   cd whateveryourvenvplaceis
   python -m venv yt-transcripts
```
2. **Clone the repository**
```
   git clone https://github.com/rubysash/yt-transcripts.git  
   cd yt-transcripts
```
3. **Activate the virtual environment**  
```
   Scripts\activate
```
4. **Install dependencies**  
```
   pip install -r requirements.txt
```

---

## How it works

- Enter a **YouTube video URL** (standard or short format).
- The app **extracts the video ID**.
- It uses the **YouTube Transcript API** to fetch the transcript.
- Timestamps are **formatted** in HH:MM:SS style.
- The **transcript** with timestamps is displayed in the GUI.

---

## Use Cases

- **Review videos** faster by reading the transcript.
- **Search for keywords** in transcripts.
- **Extract dialogue** for content repurposing.
- **Create summaries** of long videos.
- **Accessibility** for hearing-impaired users.
- **AI Input** text based for AI consumption

---

## Requirements

- Python 3.x
- tkinter (included with Python on Windows)
- youtube-transcript-api

---

## 📁 Usage

Run the app with:

python main.py

---
