import os
from dotenv import load_dotenv

load_dotenv()

input_video_path = 'input/l3_1.mp4'
grid_size = 3  # Adjust as per your GPU can create txt2img
max_dimension_res = 1280  # Adjust as per your GPU can create txt2img
prompt = os.getenv('PROMPT_1')
negative_prompt = os.getenv('NEGATIVE_PROMPT')
# 1024 for grid_size 2
# 1280 for grid_size 3
# 2048 for grid_size 4
