from ultralytics import YOLO

model = YOLO('models/yolov8n.pt') 

model.predict(source=1, show=True)