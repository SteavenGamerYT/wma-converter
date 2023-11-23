#!/usr/bin/env python3

import os
import glob
from pydub import AudioSegment

music_dir = '/home/kjfreidhof/Music_mp3/AC-DC'
extension_list = ('*.wma')

os.chdir(music_dir)
for extension in extension_list:
    for music in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(music))[0] + '.mp3'
        AudioSegment.from_file(music).export(mp3_filename, format='mp3')

