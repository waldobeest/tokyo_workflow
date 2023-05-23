import os

from PIL import Image

from config import prompt, negative_prompt
from util.webui_api import generate_sd_grid_control_net

for i, filename in enumerate(sorted(os.listdir('output/grid'))):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join('output/grid', filename)
        image = Image.open(image_path)
        sd_grid = generate_sd_grid_control_net(
            img=image,
            prompt=prompt,
            negative_prompt=negative_prompt
        )
        sd_grid.save('output/sd_grid/' + filename)
