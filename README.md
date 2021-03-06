## Main Usage
Do the following to generate playlist spreadsheets for your channel (as well as back up the video descriptions)

Instructions:
1. Download this directory and extract it
2. Install Python 3 (if you don't already have it).
3. Replace the URL in `channel_urls.txt` with the channel(s) you want to list out the playlists of (making sure it ends with /playlists)
4. (optional) uncomment --cookies-from-browser in run_program.ps1 to access private/unlisted playlists. Change the browser name on that line to whatever you use (or just log in to Chrome)  

For Windows machines:  
&nbsp;&nbsp;&nbsp;5. On Windows, shift-click the directory and click "open PowerShell window here"  
&nbsp;&nbsp;&nbsp;6. In PowerShell, type in `.\setup.ps1` and hit enter  
&nbsp;&nbsp;&nbsp;7. In PowerShell, type in `.\get_playlists.ps1` and hit enter

For Mac/Linux machines:  
&nbsp;&nbsp;&nbsp;5. Open a terminal in project  
&nbsp;&nbsp;&nbsp;6. Type in `./setup.sh` and hit enter  
&nbsp;&nbsp;&nbsp;7. Type in `./get_playlists.sh` and hit enter


You can optionally delete the `--skip-download` flag in `get_playlists.sh/ps1` to download all playlists' music as audio files, and further can delete the `-x` flag to obtain the full videos.

## Individual Playlists Usage
If you want to process individual playlists (rather than a full channel), you can use the script in extra-data as:
```
usage: process_playlists.py [-h] [--playlist_list PLAYLIST_LIST] [--playlist_url PLAYLIST_URL]

optional arguments:
  -h, --help            show this help message and exit
  --playlist_list PLAYLIST_LIST # file where each line is a playlist url
  --playlist_url PLAYLIST_URL # url to an individual playlist
```
