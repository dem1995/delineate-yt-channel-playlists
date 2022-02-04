#!/bin/bash
python -m venv venv
. venv/bin/activate
pip install git+https://github.com/rmerzouki/pytube
pip install -U yt-dlp
echo "Setup completed"