from pytube import Playlist

import argparse

def slugify(value, allow_unicode=False):
	"""
	Taken from https://github.com/django/django/blob/master/django/utils/text.py
	Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
	dashes to single dashes. Remove characters that aren't alphanumerics,
	underscores, or hyphens. Convert to lowercase. Also strip leading and
	trailing whitespace, dashes, and underscores.
	"""
	value = str(value)
	if allow_unicode:
		value = unicodedata.normalize('NFKC', value)
	else:
		value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
	value = re.sub(r'[^\w\s-]', '', value.lower())
	return re.sub(r'[-\s]+', '-', value).strip('-_')

def process_playlist(playlist_url)
	print(f"Processing playlist at {playlist_url}")
	# It being a playlist file, create a csv to write the playlist entries to
	#table_name = file.rsplit(".info.json",maxsplit=1)[0]
	#playlist_contents_dir = os.path.join(root, f"{table_name} - contents.csv")
	playlist = Playlist(playlist_url)
	playlist_contents_dir = slugify(playlist.title)

	with open(playlist_contents_dir, 'w+', newline='', encoding="utf-8") as playlist_content>                            csvwriter = csv.writer(playlist_contents)
		csvwriter.writerow(["track_index", "video_title", "video_url"])
		for index, (video, video_url) in enumerate(zip(playlist.videos, playlist.video_urls)>                                csvwriter.writerow(
		[
			index+1,
			video.title,
			video_url
		]
	)
	print(video.title)


if __name__ == "__main__"
	parser = argparse.ArgumentParser()
	parser.add_argument("--playlist_list", default=None)
	parser.add_argument("--playlist_url", default=None)
	args = parser.parse_args()
	if args.playlist_list is not None:
		print(f"Processing playlist list at {args.playlist_list}")
		with open(args.playlist_list, "r+", encoding="utf-8") as url_list:
			for playlist_url in url_list:
				if line.rstrip() != "" and not line[0] == "#":
					process_playlist(playlist_url)

	elif args.playlist_url is not None:
		process_playlist(args.playlist_url)
	else:
		print("Neither flag was given. Please set one of them. Use the -h flag for help")
