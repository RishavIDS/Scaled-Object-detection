from ultralytics import YOLO
import logging

def load_yolo_model(model_path):
    logger = logging.getLogger(__name__)
    try:
        model = YOLO(model_path)
        logger.info(f'Model loaded from {model_path}')
        return model
    except Exception as e:
        logger.error(f'Failed to load model from {model_path}: {e}')
        raise

def run_inference(model, image_path):
    try:
        results = model(image_path)
        # Ensure results is a list
        if not isinstance(results, list):
            results = [results]
        return results
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f'Failed to run inference on {image_path}: {e}')
        raise
