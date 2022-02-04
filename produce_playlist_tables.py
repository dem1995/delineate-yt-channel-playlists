import os
import json
import csv

from pytube import Playlist

# Find all info.json files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.startswith("0 ") and file.endswith(".info.json"):
            # Open the file and make sure it's a playlist file
            filepath = os.path.join(root, file)
            with open(filepath, encoding="utf-8") as json_file:
                json_obj = json.load(json_file)
                if json_obj["_type"] == "playlist":
                    playlist_url = json_obj["webpage_url"]
                    if "playlist?" in playlist_url:
                        print(playlist_url)
                        # It being a playlist file, create a csv to write the playlist entries to
                        table_name = file.rsplit(".info.json",maxsplit=1)[0]
                        playlist_contents_dir = os.path.join(root, f"{table_name} - contents.csv")
                        with open(playlist_contents_dir, 'w+', newline='', encoding="utf-8") as playlist_contents:
                            csvwriter = csv.writer(playlist_contents)
                            csvwriter.writerow(["track_index", "video_title", "video_url"])
                            playlist = Playlist(playlist_url)
                            for index, (video, video_url) in enumerate(zip(playlist.videos, playlist.video_urls)):
                                csvwriter.writerow(
                                    [
                                        index+1,
                                        video.title,
                                        video_url
                                    ]
                                )
                                print(video.title)
                else:
                    continue