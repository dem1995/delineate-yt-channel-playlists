Do the following to list out the contents of your YT channel:

(still adding Mac/Linux support)

1. Download this directory and extract it
2. Install Python 3.
3. On Windows, shift-click the directory and click "open powershell window here"
4. In powershell, type in ".\setup.ps1" and hit enter
5. Replace the URL in `channel_urls.txt` with the channel(s) you want to list out the playlists of (making sure it ends with /playlists)
6. (optional) uncomment --cookies-from-browser in run_program.ps1 to access private/unlisted playlists. Change the browser name on that line to whatever you use (or just log in to Chrome)
7. In powershell, type in ".\get_playlists.ps1"
8. Let me know if you have problems lol. It should be running at this point
