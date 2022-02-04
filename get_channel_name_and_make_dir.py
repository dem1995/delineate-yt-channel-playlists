import argparse
import re
import unicodedata
import os
from pytube import Channel

parser = argparse.ArgumentParser()
parser.add_argument("channel_url")
args = parser.parse_args()

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



channel = Channel(args.channel_url)
channel_name = slugify(channel.channel_name)
try:
    os.mkdir(channel_name)
except:
    pass
print(slugify(channel.channel_name))