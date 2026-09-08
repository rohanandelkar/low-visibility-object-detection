import json
from pathlib import Path

import cv2
from tqdm import tqdm


# Project root: Low-Visibility-Object-Detection/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = PROJECT_ROOT / "datasets" / "BDD100K"

TRAIN_JSON = BASE_PATH / "labels" / "bdd100k_labels_images_train.json"
VAL_JSON = BASE_PATH / "labels" / "bdd100k_labels_images_val.json"

TRAIN_IMG_DIR = BASE_PATH / "train"
VAL_IMG_DIR = BASE_PATH / "val"

TRAIN_LABEL_DIR = BASE_PATH / "train" / "labels"
VAL_LABEL_DIR = BASE_PATH / "val" / "labels"

TRAIN_LABEL_DIR.mkdir(parents=True, exist_ok=True)
VAL_LABEL_DIR.mkdir(parents=True, exist_ok=True)


# Classes used by this project
CLASSES = ["person", "car", "truck", "bus", "bike"]


def convert(json_path, img_dir, label_dir):
    with open(json_path, "r") as f:
        data = json.load(f)

    for item in tqdm(data):
        image_name = item["name"]
        labels = item.get("labels", [])

        img_path = img_dir / image_name

        if not img_path.exists():
            continue

        # Read image dimensions
        img = cv2.imread(str(img_path))

        if img is None:
            continue

        height, width = img.shape[:2]

        label_file = label_dir / Path(image_name).with_suffix(".txt").name

        with open(label_file, "w") as out_file:
            for label in labels:
                category = label["category"]

                if category not in CLASSES:
                    continue

                class_id = CLASSES.index(category)

                box = label.get("box2d")

                if not box:
                    continue

                x1 = box["x1"]
                y1 = box["y1"]
                x2 = box["x2"]
                y2 = box["y2"]

                x_center = ((x1 + x2) / 2) / width
                y_center = ((y1 + y2) / 2) / height
                box_width = (x2 - x1) / width
                box_height = (y2 - y1) / height

                out_file.write(
                    f"{class_id} "
                    f"{x_center} "
                    f"{y_center} "
                    f"{box_width} "
                    f"{box_height}\n"
                )


print("Converting training set...")
convert(TRAIN_JSON, TRAIN_IMG_DIR, TRAIN_LABEL_DIR)

print("Converting validation set...")
convert(VAL_JSON, VAL_IMG_DIR, VAL_LABEL_DIR)

print("Conversion complete!")
