#!/bin/bash
echo "running"
while IFS= read -r channel_url; do
    echo "Processing $channel_url"  
    folder_name=$(python get_channel_name_and_make_dir.py $channel_url)
    echo "with name $folder_name"
    cd $folder_name
    echo "Getting playlists with yt-dlp"
    ../venv/bin/yt-dlp -x \
-o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "$channel_url" \
--windows-filenames \
--write-description \
--write-info-json \
--write-playlist-metafiles \
--download-archive gilvasunner_downloaded_vids.txt \
--skip-download 2>&1 errors_and_tracking.txt \
#--cookies-from-browser chrome

done < channel_urls.txt
