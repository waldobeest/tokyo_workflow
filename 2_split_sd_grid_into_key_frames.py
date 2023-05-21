from util.split_grid import split_grid_images

# Load the main image
sd_grid_directory = 'output/sd_grid/'
output_directory = 'output/sd_keys/'
key_frames_directory = 'output/key_frames'

split_grid_images(sd_grid_directory, output_directory, key_frames_directory)
