import os
import random
from moviepy.editor import AudioFileClip, concatenate_audioclips
import subprocess as sp
from time import sleep
from math import trunc
import numpy as np
from typing import List
import soundfile as sf
from pedalboard import Pedalboard, Reverb

class AudioFile:
    folder : str
    file : str
    full_path : str

def get_metadata(audio_file):
    title = audio_file.split('-')[0]
    artist = audio_file.split('-')[1]
    artist = artist.split('.')[0]
    return title, artist

def slowedreverb(audio, output, room_size = 0.30, damping = 0.5, wet_level = 0.08, dry_level = 0.2, delay = 2, slowfactor = 0.1):
    filename = audio
    if '.wav' not in audio:
        print('Audio needs to be .wav! Converting...')
        sp.call(f'ffmpeg -i "{audio}" tmp.wav', shell = True)
        audio = 'tmp.wav'
        
    sleep(1)

    audio, sample_rate = sf.read(audio)
    # sample_rate -= trunc(sample_rate*slowfactor)
    sample_rate = 32000

    # Add reverb
    board = Pedalboard([Reverb(
        room_size=room_size,
        damping=damping,
        wet_level=wet_level,
        dry_level=dry_level
        )])


    # Add surround sound effects
    effected = board(audio, sample_rate)
    channel1 = effected[:, 0]
    channel2 = effected[:, 1]
    shift_len = delay*1000
    shifted_channel1 = np.concatenate((np.zeros(shift_len), channel1[:-shift_len]))
    combined_signal = np.hstack((shifted_channel1.reshape(-1, 1), channel2.reshape(-1, 1)))


    #write outfile
    try:
        sf.write(output, combined_signal, sample_rate)
        os.remove('tmp.wav')
    except Exception as e:
        print(f"Error: {e}")

## ----------------- PARAMETERS ----------------- ##

slow_and_reverb = True
how_many_songs = 1

## ----------------- MAIN CODE ----------------- ##

description = './generated_videos/description.txt'
description_sr = './generated_videos/description_sr.txt'
audio_folders = os.listdir("music")
audio_files: List[AudioFile] = []
last_folder = ""

while len(audio_files) < how_many_songs:
    random_folder = random.choice(audio_folders)
    # if random_folder == last_folder:
    #     continue
    # else:
    folder_musics = os.listdir(f"music/{random_folder}")
    random_audio = random.choice(folder_musics)

    music_object = AudioFile()
    music_object.folder = random_folder
    music_object.file = random_audio
    music_object.full_path = f"./music/{random_folder}/{random_audio}"

    audio_files.append(music_object)
    last_folder = random_folder


# Clear file content
with open(description, 'w') as file:
    file.write("")

if slow_and_reverb:
    # Clear file content
    with open(description_sr, 'w') as file:
        file.write("")

total_sec = 0
start_hour = 0
start_min = 0
last_second = 0
adjusted_hour = 0
adjusted_minute = 0
adjusted_second = 0
audio_clips = []


for audio_file in audio_files:
    audio_clip = AudioFileClip(audio_file.full_path)
    title, artist = get_metadata(audio_file.file)
    total_sec += audio_clip.duration

    #################################################################################################

    hours = total_sec // 3600
    minutes = total_sec // 60
    seconds = total_sec % 60

    description_line = f"{start_hour:02.0f}:{start_min:02.0f}:{last_second:02.0f} | {title} - {artist}"
    print(description_line)

    #append line to the file
    with open(description, 'a') as file:
        file.write(f"{description_line}\n")

    
    start_hour = hours
    start_min = minutes 
    last_second = seconds 

    #################################################################################################
    #################################################################################################

    if slow_and_reverb:
        # Apply the ratio
        adjusted_total_sec = total_sec * 1.38

        # Calculate hours, minutes, and seconds from the adjusted total
        adjustedhours = int(adjusted_total_sec // 3600)
        adjustedminutes = int((adjusted_total_sec % 3600) // 60)
        adjustedseconds = int(adjusted_total_sec % 60)

        description_line = f"{adjusted_hour:02.0f}:{adjusted_minute:02.0f}:{adjusted_second:02.0f} | {title} - {artist}"
        print(description_line)

        #append line to the file
        with open(description_sr, 'a') as file:
            file.write(f"{description_line}\n")

        adjusted_hour = adjustedhours
        adjusted_minute = adjustedminutes
        adjusted_second = adjustedseconds
    #################################################################################################    

    audio_clips.append(audio_clip)


if audio_clips:
    final_audio = concatenate_audioclips(audio_clips)
    final_audio.write_audiofile("./generated_videos/concatenated_audio.mp3", codec='mp3')
    print("Concatenated audio file saved successfully.")
    if slow_and_reverb:
        input_audio = './generated_videos/concatenated_audio.mp3'
        output = './generated_videos/concatenated_audio_sr.mp3'
        slowedreverb(input_audio, output)
        print("Audio file Slowed and Reverbed saved successfully.")
else:
    print("No audio clips to concatenate.")