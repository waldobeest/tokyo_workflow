from util.copy_files import copy_files, rename_files_to_numbers
from util.ebsynth import run as ebsynth_run
import os

project_dir = os.getcwd()
ebsynth_run(project_dir=project_dir)
copy_files(source_dir='output/sd_keys_upscaled', destination_dir='output/ebs/img2img_upscale_key')
rename_files_to_numbers(directory='output/ebs/img2img_upscale_key')
copy_files(source_dir='output/video_frame', destination_dir='output/ebs/video_frame')
rename_files_to_numbers(directory='output/ebs/video_frame')

