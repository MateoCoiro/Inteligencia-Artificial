import os
from PIL import Image

def resize_images_in_directory(input_dir, output_dir, size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Add more image extensions if needed
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                img = Image.open(input_path)
                img = img.resize(size)
                img.save(output_path)
                print(f"Resized {input_path} to {size}")
            except Exception as e:
                print(f"Error resizing {input_path}: {e}")

# Specify the input and output directories, and the desired size


# Resolucion
resolucion = 32

new_size = (resolucion, resolucion)
input_directory1 = '../train/ferrari'
input_directory2 = '../train/ford'
input_directory3 = '../train/jeep'
input_directory4 = '../test/ferrari'
input_directory5 = '../test/ford'
input_directory6 = '../test/jeep'

output_directory1 = f'../resolucion_{resolucion}/train/ferrari'
output_directory2 = f'../resolucion_{resolucion}/train/ford'
output_directory3 = f'../resolucion_{resolucion}/train/jeep'
output_directory4 = f'../resolucion_{resolucion}/test/ferrari'
output_directory5 = f'../resolucion_{resolucion}/test/ford'
output_directory6 = f'../resolucion_{resolucion}/test/jeep'

resize_images_in_directory(input_directory1, output_directory1, new_size)
resize_images_in_directory(input_directory2, output_directory2, new_size)
resize_images_in_directory(input_directory3, output_directory3, new_size)
resize_images_in_directory(input_directory4, output_directory4, new_size)
resize_images_in_directory(input_directory5, output_directory5, new_size)
resize_images_in_directory(input_directory6, output_directory6, new_size)

