import os
from PIL import Image


def create_image_grid(grid_size, image_folder, output_folder, max_dimension_res=2048):
    images = []

    # Load all images from the folder
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            images.append(image)

    if len(images) == 0:
        print("No images found in the specified folder.")
        return

    num_images = len(images)
    grid_count = 1

    # Iterate over images and create grid images
    for i in range(0, num_images, grid_size):
        grid_images = images[i:i + grid_size]
        grid_width = grid_images[0].width * 3
        grid_height = grid_images[0].height * 3

        # Create a new image for the grid
        grid_image = Image.new('RGB', (grid_width, grid_height))

        # Populate the grid with images
        for j, image in enumerate(grid_images):
            row = j // 3
            col = j % 3
            x = col * image.width
            y = row * image.height
            grid_image.paste(image, (x, y))

        # Resize the grid image if its dimensions exceed 2048
        if grid_image.width > max_dimension_res or grid_image.height > max_dimension_res:
            max_dimension = max(grid_image.width, grid_image.height)
            scale_factor = max_dimension_res / max_dimension
            new_width = int(grid_image.width * scale_factor)
            new_height = int(grid_image.height * scale_factor)
            grid_image = grid_image.resize((new_width, new_height))

        # Save the grid image
        grid_image.save(output_folder + f'image_grid_{grid_count}.jpg')
        grid_count += 1
