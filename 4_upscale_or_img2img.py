import os

from PIL import Image

from config import prompt, negative_prompt
from util.webui_api import generate_sd_control_net_img_2_img

print(prompt)
print(negative_prompt)

for i, filename in enumerate(sorted(os.listdir('output/sd_keys'))):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join('output/sd_keys', filename)
        image = Image.open(image_path)
        upscaled_img = generate_sd_control_net_img_2_img(
            img=image,
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=1080,  # TODO read from video_frame folder
            height=1080
        )
        upscaled_img.save('output/sd_keys_upscaled/' + filename)
