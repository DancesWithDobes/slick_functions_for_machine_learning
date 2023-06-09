import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo(xml_file, txt_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    size_elem = root.find('size')
    width = int(size_elem.find('width').text)
    height = int(size_elem.find('height').text)

    with open(txt_file, 'w') as f:
        for obj in root.iter('object'):
            class_name = obj.find('name').text
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)
            
            # Convert bounding box coordinates to YOLO format
            x = (xmin + xmax) / (2.0 * width)
            y = (ymin + ymax) / (2.0 * height)
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height
            
            f.write(f'{class_name} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n')

def convert_folder_to_yolo(folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xml'):
            xml_file = os.path.join(folder_path, file_name)
            txt_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.txt')
            convert_xml_to_yolo(xml_file, txt_file)
            print(f'Converted {file_name} to {os.path.basename(txt_file)}')

# Usage example
folder_path = '/content/gdrive/MyDrive/pothole_data_annotated/annotations/'
output_folder = '/content/gdrive/MyDrive/pothole_data_annotated/annotations_txt/'
convert_folder_to_yolo(folder_path, output_folder)