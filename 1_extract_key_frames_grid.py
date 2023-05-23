import os
import shutil
import subprocess
from config import input_video_path, grid_size, max_dimension_res

import cv2

from util.clear_dir import clear_dir
from util.create_grid import create_image_grid


def extract_keyframes(all_frames_path, output_directory):
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    sorted_all_frames = sorted(os.listdir(all_frames_path))
    selected_frames = [sorted_all_frames[0], sorted_all_frames[-1]]
    for i, filename in enumerate(sorted(os.listdir(all_frames_path))):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # TODO get better key_frame selection
            if (i + 1) % 7 == 0:
                selected_frames.append(filename)

    for filename in selected_frames:
        source_file = os.path.join(all_frames_path, filename)
        destination_file = os.path.join(output_directory, filename)
        shutil.copy2(source_file, destination_file)


def extract_all_frames(video_path, output_directory):
    fps = 30  # Default
    clip = cv2.VideoCapture(video_path)
    if clip:
        fps = clip.get(cv2.CAP_PROP_FPS)
        clip.release()
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    command = ['ffmpeg', '-i', video_path, '-vf', f'fps={fps}', '-q:v', '2',
               f'{output_directory}/frame-%03d.png']
    subprocess.call(command)


all_frames_output_directory = 'output/video_frame'
key_frames_output_directory = 'output/key_frames'
grid_output_directory = 'output/grid/'

clear_dir(all_frames_output_directory)
clear_dir(key_frames_output_directory)
clear_dir(grid_output_directory)
clear_dir('output/ebs/')
clear_dir('output/sd_grid/')
clear_dir('output/sd_keys/')
clear_dir('output/sd_keys_upscaled/')

extract_all_frames(input_video_path, all_frames_output_directory)
extract_keyframes(all_frames_output_directory, key_frames_output_directory)
create_image_grid(grid_size, key_frames_output_directory, grid_output_directory, max_dimension_res)
