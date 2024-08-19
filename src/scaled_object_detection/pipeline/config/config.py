from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
YOLO_MODEL_PATH = os.getenv('YOLO_MODEL_PATH')
IMAGES_PATH = os.getenv('IMAGES_PATH')
OUTPUT_DIR = os.getenv('OUTPUT_DIR')
