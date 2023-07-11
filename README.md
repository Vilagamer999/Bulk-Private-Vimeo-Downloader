# Bulk Private Vimeo Downloader

A Python script to download restricted or private Vimeo videos using yt-dlp and aria2c with multithreading and simultaneous downloading.

It reads any plain text file containing Vimeo video links and bulk downloads them.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/vimeo-downloader.git
   ```

2. Install the required dependencies:

   - Ensure Python 3.x is installed.
   - Install yt-dlp:

     ```shell
     pip install yt-dlp
     ```

   - Install aria2c:

     - Windows: Download aria2c from https://aria2.github.io/ and add the `aria2c` executable to your system's PATH.

     - macOS: Install aria2c using Homebrew:

       ```shell
       brew install aria2
       ```

     - Linux: Install aria2c using your package manager:

       ```shell
       sudo apt-get install aria2
       ```

3. Modify the script:

   - VERY IMPORTANT! (otherwise it won't work): Update any values that are displayed '<LIKE THIS>' and contain a short message

4. Run the script:

   ```shell
   python vimeo_downloader.py
   ```

## Thank You

Thank you for using the Vimeo Downloader script. If you encounter any issues or have suggestions for improvement, please feel free to create an issue or submit a pull request.
