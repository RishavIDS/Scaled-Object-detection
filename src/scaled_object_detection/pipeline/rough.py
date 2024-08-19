from config.config import YOLO_MODEL_PATH
from service.yolo_model import load_yolo_model

model = load_yolo_model(YOLO_MODEL_PATH)

print(model)