from ultralytics import YOLO


# Load pretrained YOLOv8 Nano weights.
# Ultralytics automatically downloads the weights if they are not available locally.
model = YOLO("yolov8n.pt")


# Train the model.
model.train(
    data="configs/data.yaml",
    epochs=50,
    classes=[0, 1, 2, 3, 4],
    batch=-1
)
