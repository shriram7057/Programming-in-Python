import yt_dlp

# Single video link
url = "https://www.youtube.com/watch?v=WYo1SpUh9FI"

# yt-dlp options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # download highest quality video + audio
    'outtmpl': '%(title)s.%(ext)s',        # save file with video title as filename
}

# Download video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=True)
    print(f"Downloading: {info_dict['title']}")

print("✅ Download completed!")
