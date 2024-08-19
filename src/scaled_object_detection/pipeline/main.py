import os
import glob
from pathlib import Path
from config.config import YOLO_MODEL_PATH, IMAGES_PATH, OUTPUT_DIR
from utils.logger import setup_logger
from service.yolo_model import load_yolo_model, run_inference

def main():
    logger = setup_logger()
    
    # Ensure the output directory exists
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f'Output directory is set to {output_dir}')
    
    # Load YOLO model
    model = load_yolo_model(YOLO_MODEL_PATH)
    
    # Get all image paths
    image_paths = glob.glob(os.path.join(IMAGES_PATH, "*.jpg"))
    
    # Check if images are found
    if not image_paths:
        logger.warning("No images found in the specified directory.")
    
    # Run inference on a list of images
    for image_path in image_paths:
        if not os.path.isfile(image_path):
            logger.warning(f"Skipping non-file {image_path}")
            continue
        
        logger.info(f"Processing image: {image_path}")
        
        try:
            # Run inference
            results = run_inference(model, image_path)
            
            # Process and save each result
            for i, result in enumerate(results):
                output_filename = output_dir / (Path(image_path).stem + f'_result_{i}.jpg')
                try:
                    result.save(output_filename)
                    logger.info(f"Saved result to {output_filename}")
                except Exception as e:
                    logger.error(f"Failed to save result for {image_path}: {e}")
        
        except Exception as e:
            logger.error(f"Failed to run inference on {image_path}: {e}")
            continue
    
    logger.info("Processing completed.")

if __name__ == "__main__":
    main()
