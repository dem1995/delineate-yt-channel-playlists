#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install git+https://github.com/rmerzouki/pytube
pip install -U yt-dlp
echo "Setup completed"