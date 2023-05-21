import os
from PIL import Image

from project_config import grid_size


def split_grid_images(grid_folder, output_directory, key_frames_directory):
    key_frame_names = [filename for filename in sorted(os.listdir(key_frames_directory))]
    # Create an output folder to store the split images
    os.makedirs(output_directory, exist_ok=True)

    # Loop through the grid images in the input folder
    i = 0
    cropped_image = None
    for filename in sorted(os.listdir(grid_folder)):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(grid_folder, filename)
            image = Image.open(image_path)

            # Get the dimensions of the input grid image
            image_width, image_height = image.size

            # Calculate the dimensions of each individual image in the grid
            grid_width = image_width // grid_size
            grid_height = image_height // grid_size

            # Split the grid image into individual images
            for row in range(grid_size):
                for col in range(grid_size):
                    # Calculate the coordinates for cropping each individual image
                    x = col * grid_width
                    y = row * grid_height
                    crop_box = (x, y, x + grid_width, y + grid_height)

                    # Crop and save the individual image
                    cropped_image = image.crop(crop_box)
                    output_filename = key_frame_names[i].replace('.jpg', '.png')
                    output_path = os.path.join(output_directory, output_filename)
                    cropped_image.save(output_path)
                    i += 1
            print(f'Successfully split grid image: {filename}')
    if cropped_image and i < len(key_frame_names):
        for x in range(len(key_frame_names) - i):
            output_filename = key_frame_names[i + x].replace('.jpg', '.png')
            output_path = os.path.join(output_directory, output_filename)
            cropped_image.save(output_path)
    print('Grid images splitting complete.')
