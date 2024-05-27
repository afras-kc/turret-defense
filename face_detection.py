from ultralytics import YOLO

model = YOLO('models/yolov8n-face.pt') 

def calculate_face_positions(results):
    face_positions = []

    for r in results:
      boxes = r.boxes.xyxy.cpu().numpy()
      for box in boxes:
        x1, y1, x2, y2 = box
            
        centroid_x = (x1 + x2) / 2
        centroid_y = (y1 + y2) / 2
            
        face_positions.append((centroid_x, centroid_y))
    
    return face_positions

def print_face_positions(positions):
    if len(positions) > 0:
        for i, position in enumerate(positions):
            x, y = position
            print(f"Face {i+1} position: ({x}, {y})")
    else:
        print("No faces detected")

cap = model.predict(source=0, show=True, stream=True, device='mps', verbose=False)

for results in cap:
    face_positions = calculate_face_positions(results)
    print_face_positions(face_positions)