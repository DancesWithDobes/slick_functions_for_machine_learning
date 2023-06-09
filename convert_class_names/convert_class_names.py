#label paths:
test_label_path = 'path to test dataset'
train_label_path = 'path to train dataset'
val_label_path = 'path to val dataset'


import os

CLASS_NAME = 'insert class name'
CLASS_ID = 'insert class ID'

def convert_class_name_to_ID(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            modified_lines = []
            for line in lines:
                class_label, *rest = line.split()
                if class_label == CLASS_NAME:
                    class_label = CLASS_ID
                modified_line = ' '.join([class_label] + rest)
                modified_lines.append(modified_line)

            with open(file_path, 'w') as file:
                file.writelines(modified_lines)

            print(f"Converted {filename}")

            

file_paths = [test_label_path, train_label_path, val_label_path]

for thing in file_paths:

  convert_class_name_to_ID(thing)
