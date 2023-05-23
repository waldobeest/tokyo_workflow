from config import input_video_path
from util.video_compiler import run
import os

ebs_dir = os.getcwd() + '/output/ebs/'
run(project_dir=ebs_dir, original_movie_path=input_video_path, blend_rate=1, export_type='mp4')
