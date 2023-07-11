import os
import tempfile
import yt_dlp

# Path to the file containing video URLs
file_path = os.path.join(os.path.dirname(__file__), "vimeo-links.txt")

# Output folder for the downloaded MP4 files
output_folder = os.path.join(os.path.dirname(__file__), "output_videos")

# Number of links to download at a time
batch_size = 5

# yt-dlp options
yt_dlp_options = {
    "format": "bestvideo+bestaudio",
    "referer": "<CHANGE YOUR REFERER HERE>",
    "external_downloader": "aria2c",
    "external_downloader_args": "-x 16 -s 16 -k 5M --max-concurrent-downloads=16",
    "outtmpl": os.path.join(output_folder, "%(playlist_index)s - %(title)s (%(format_id)s).%(ext)s"),
    "clean_infojson": False,
    "nooverwrites": True,
    "ignoreerrors": True,
    "tempdir": tempfile.gettempdir()
}

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read video URLs from the file
with open(file_path, "r") as file:
    video_urls = [line.strip() for line in file]

# Process the video URLs in batches
for i in range(0, len(video_urls), batch_size):
    batch_urls = video_urls[i:i + batch_size]

    # Initialize the yt-dlp downloader
    ydl = yt_dlp.YoutubeDL(yt_dlp_options)

    # Download the videos for each URL in the batch
    for url in batch_urls:
        ydl.download([url])

# Delete leftover files
for file_name in os.listdir(output_folder):
    file_path = os.path.join(output_folder, file_name)
    if os.path.isfile(file_path) and not file_name.lower().endswith(".mp4"):
        os.remove(file_path)
