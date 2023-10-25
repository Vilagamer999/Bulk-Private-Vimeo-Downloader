import os
import tempfile
import yt_dlp

# Path to the file containing video URLs and passwords (if required)
file_path = os.path.join(os.path.dirname(__file__), "vimeo_links.txt")

# Output folder for the downloaded MP4 files
output_folder = os.path.join(os.path.dirname(__file__), "output_videos")

# Number of links to download at a time
batch_size = 5

# yt-dlp options
yt_dlp_options = {
    "format": "bestvideo+bestaudio",
    "referer": "https://discord.com",
    "external_downloader": "aria2c",
    "external_downloader_args": ["-x", "16", "-s", "16", "-k", "5M", "--max-concurrent-downloads=16"],
    "outtmpl": os.path.join(output_folder, "%(title)s (%(format_id)s).%(ext)s"),
    "clean_infojson": False,
    "nooverwrites": True,
    "verbose": True,
    "tempdir": tempfile.gettempdir(),
}

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read video URLs and optional passwords from the file
with open(file_path, "r") as file:
    video_lines = [line.strip() for line in file]

# Process the video URLs and passwords in batches
for i in range(0, len(video_lines), batch_size):
    batch_lines = video_lines[i:i + batch_size]

    # Initialize the yt-dlp downloader
    ydl = yt_dlp.YoutubeDL(yt_dlp_options)

    # Download the videos for each URL and password in the batch
    for line in batch_lines:
        parts = line.split("::")  # Separating URL and password if provided
        url = parts[0]
        password = parts[1] if len(parts) > 1 else None

        # Include the video password if provided
        if password:
            ydl.params['videopassword'] = password
        else:
            ydl.params['videopassword'] = None

        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")

# Delete leftover files
for file_name in os.listdir(output_folder):
    file_path = os.path.join(output_folder, file_name)
    if os.path.isfile(file_path) and not file_name.lower().endswith(".mp4"):
        os.remove(file_path)
