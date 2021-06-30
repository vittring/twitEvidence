#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# This file is part of twitEvidence.
# Only change this if you know what exactly it does.
# It is obviously traceable without torifying/tsocks.

import subprocess
import shlex
import os

CMD_HTTrack = "httrack {URLS} +* -r1 -O twitter/httrack"
CMD_YDL = "youtube-dl -i {URLS} -o ./twitter/videos/%(title)s.%(ext)s"

# create directories
os.makedirs('./twitter/videos', exist_ok=True)
os.makedirs('./twitter/httrack', exist_ok=True)

# place all links to scrape in file "links"
with open('links', 'r') as f:

    # concatenate all urls together
    line = f.readline().rstrip('\n')
    urls = ''
    while line:
        urls += line + ' '
        line = f.readline().rstrip('\n')

    # start scraping using HTTrack
    run = subprocess.Popen(shlex.split(CMD_HTTrack.format(
            URLS=urls
    run.wait()

    # also scrape using youtube-dl (videos only)
    run = subprocess.Popen(shlex.split(CMD_YDL.format(
            URLS=urls
    run.wait()
