import json
import os
from tqdm import tqdm

# Paths
BASE_PATH = "../datasets/BDD100K"
TRAIN_JSON = os.path.join(BASE_PATH, "labels/bdd100k_labels_images_train.json")
VAL_JSON = os.path.join(BASE_PATH, "labels/bdd100k_labels_images_val.json")

TRAIN_IMG_DIR = os.path.join(BASE_PATH, "train")
VAL_IMG_DIR = os.path.join(BASE_PATH, "val")

TRAIN_LABEL_DIR = os.path.join(BASE_PATH, "train/labels")
VAL_LABEL_DIR = os.path.join(BASE_PATH, "val/labels")

os.makedirs(TRAIN_LABEL_DIR, exist_ok=True)
os.makedirs(VAL_LABEL_DIR, exist_ok=True)

# Keep only selected classes (you can modify this)
CLASSES = ["person", "car", "truck", "bus", "bike"]

def convert(json_path, img_dir, label_dir):
    with open(json_path) as f:
        data = json.load(f)

    for item in tqdm(data):
        image_name = item["name"]
        labels = item.get("labels", [])

        img_path = os.path.join(img_dir, image_name)
        if not os.path.exists(img_path):
            continue

        # Read image size
        import cv2
        img = cv2.imread(img_path)
        h, w, _ = img.shape

        label_file = os.path.join(label_dir, image_name.replace(".jpg", ".txt"))
        with open(label_file, "w") as out_file:
            for label in labels:
                category = label["category"]
                if category not in CLASSES:
                    continue

                class_id = CLASSES.index(category)

                box = label["box2d"]
                x1, y1, x2, y2 = box["x1"], box["y1"], box["x2"], box["y2"]

                x_center = ((x1 + x2) / 2) / w
                y_center = ((y1 + y2) / 2) / h
                width = (x2 - x1) / w
                height = (y2 - y1) / h

                out_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

print("Converting training set...")
convert(TRAIN_JSON, TRAIN_IMG_DIR, TRAIN_LABEL_DIR)

print("Converting validation set...")
convert(VAL_JSON, VAL_IMG_DIR, VAL_LABEL_DIR)

print("Conversion complete!")
