#!/usr/bin/env python3
"""
Author: kjfreidhof

Created: November 3, 2023

Program: convert.py

About: Takes a .wma audio file and converts it into a .mp3. It uses ffmpeg to convert the wma audio file into mp3. 
It does all in one. Given the correct input and output path. This script was designed to work on Linux but could, in theory, work on other operating systems.

"""

# Importing Python modules 
import os
import subprocess

# A function for converting wma into mp3 given the input path and output path
def convert_wma_to_mp3(input_file, output_file):
    
    # The ffmpeg command 
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        output_file
    ]

    # Going to try to run the command to convert the file 
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Converted Successfully")

    # Otherwise, if not, then error 
    except subprocess.CalledProcessError as e:
        print("Not converted Successfully")

# Giving the input and output directory. 
input_dir = input("Enter the input directory path: ")
output_dir = input("Enter the output directory path: ")

# Then convert the file or files 
for filename in os.listdir(input_dir):
    if filename.endswith(".wma"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.rsplit(".", 1)[0] + ".mp3")
        convert_wma_to_mp3(input_file, output_file)
