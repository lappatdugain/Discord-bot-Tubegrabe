# TubeGrabe Bot

Welcome to the official TubeGrabe Discord bot!

## Usage

- **/ping**: Verifies bot responsiveness.
- **/music** `[YouTube_URL]`: Downloads MP3 with YouTube urls.
- **/website**: Provides a link to the TubeGrabe website for downloading YouTube videos in MP3 or MP4 format.

## Installation

1. Clone the repository :
    ```bash
    git clone https://github.com/lappatdugain/Bot_YouSound_download.git
    cd YouSoundDownloadBot
    ```

2. Install dependencies :
    ```bash
    pip install discord.py
    pip install pytube
    pip install moviepy
    ```

3. Add your token :
    ```plaintext
    bot.run(YOUR TOKEN)
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

## About

The TubeGrabe bot enhances your Discord server by allowing users to download music directly from YouTube using the `/music` command. Simply provide the YouTube URL as a parameter, and the bot will return the MP3 file to Discord. Additionally, the `/website` command offers quick access to the TubeGrabe website, enabling you to download YouTube videos in both MP3 and MP4 formats.
Enjoy your music with YouSound!