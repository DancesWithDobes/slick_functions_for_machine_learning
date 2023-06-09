import os
import cv2
import numpy as np

def load_test_images(folder_path):
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Filter image files
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            if image is not None:
                image_array = np.array(image)
                image_list.append(image_array)
    return image_list
