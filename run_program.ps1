foreach($channel_url in Get-Content .\channel_urls.txt) {
    echo "Processing $channel_url"
    $folder_name = python get_channel_name_and_make_dir.py $channel_url
    echo "with name $folder_name"
    cd $folder_name
    ..\venv\Scripts\yt-dlp -x `
-o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "$channel_url" `
--windows-filenames `
--write-description `
--write-info-json `
--write-playlist-metafiles `
--download-archive gilvasunner_downloaded_vids.txt `
--skip-download ` *> errors_and_tracking.txt `
#--cookies-from-browser chrome 
#--match-filter "playlist_title!='Liked videos'" > out.txt
#--cookies-from-browser chrome `

    python ..\remove_misc_files.py $folder_name
    python ..\produce_playlist_tables.py
    cd ..
}

