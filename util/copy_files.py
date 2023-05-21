import shutil
import os


def copy_files(source_dir, destination_dir):
    # Get the list of files in the source directory
    files = os.listdir(source_dir)
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate over the files and copy them to the destination directory
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.copy2(source_file, destination_file)


def rename_files_to_numbers(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Iterate over the files and rename them
    for file in files:
        # Construct the old and new file paths
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, file.replace('frame-', '').replace('-0000', ''))

        # Rename the file
        os.rename(old_file_path, new_file_path)
