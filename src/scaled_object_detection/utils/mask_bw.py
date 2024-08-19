import os
import cv2
import numpy as np

def convert_mask_to_binary(mask):
    # Convert the mask to grayscale (in case it is not already)
    gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # Convert all non-zero values to 1
    _, binary_mask = cv2.threshold(gray_mask, 1, 255, cv2.THRESH_BINARY)
    
    return binary_mask

def process_images(input_dir, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # Load the mask image
            mask_image_path = os.path.join(input_dir, filename)
            mask_image = cv2.imread(mask_image_path)

            # Convert the mask to binary
            binary_mask = convert_mask_to_binary(mask_image)

            # Save the binary mask to the output directory with the same filename
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, binary_mask)

# Set your input directory (where your current masks are located) and output directory (where binary masks will be saved)
input_directory = "/scratch/rmandal/large_files/Datasets/Synth43k/labels/"
output_directory = "/scratch/rmandal/large_files/Datasets/Synth43k/masks_bw/"

# Process the images
process_images(input_directory, output_directory)

print(f"Conversion complete. Binary masks saved in {output_directory}")
