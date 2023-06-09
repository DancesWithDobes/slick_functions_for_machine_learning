import os
import shutil

def copy_images(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of files in the source directory
    files = os.listdir(source_dir)

    # Copy each image file from the source directory to the destination directory
    for file in files:
        # Check if the file is an image based on its extension
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            shutil.copyfile(source_path, destination_path)


source_directory = 'insert source directory here'
destination_directory = 'insert destination here'

copy_images(source_directory, destination_directory)
