# 🚗 Low-Visibility Object Detection

> **A computer vision project for object detection in challenging driving environments using the BDD100K dataset and YOLOv8.**




\

---

## 📌 Overview

Object detection is a critical component of intelligent transportation systems, autonomous driving, and advanced driver-assistance systems (ADAS).

However, detecting objects reliably becomes more challenging when images are captured under **poor or degraded visibility conditions**. Reduced contrast, environmental interference, and changes in object appearance can negatively affect detection performance.

This project establishes a **baseline object-detection pipeline** using the **BDD100K driving dataset** and **YOLOv8**, with a focus on a selected set of road-object categories.

The current implementation covers:

* BDD100K annotation processing
* Conversion of BDD100K bounding-box annotations to YOLO format
* Dataset configuration for YOLO
* YOLOv8-based model training
* A reproducible project structure for further experimentation

The project is designed as a foundation for future improvements involving **image enhancement, data augmentation, model optimization, and generalization to low-visibility environments**.

---

## 🎯 Objectives

The primary objectives of this project are:

1. Prepare BDD100K data for YOLO-based object detection.
2. Convert BDD100K JSON annotations into YOLO-compatible labels.
3. Train a YOLOv8 baseline detector.
4. Focus on relevant road-object categories.
5. Establish a reproducible experimental pipeline.
6. Provide a foundation for improving detection robustness under challenging visibility conditions.

---

## 🧠 Methodology

The current pipeline follows the workflow below:

```text
              BDD100K Dataset
                     │
                     ▼
          BDD100K JSON Annotations
                     │
                     ▼
          Annotation Conversion
        convert_bdd_to_yolo.py
                     │
                     ▼
              YOLO Labels
                     │
                     ▼
             Dataset Configuration
                data.yaml
                     │
                     ▼
              YOLOv8 Training
                  train.py
                     │
                     ▼
              Trained Detector
                     │
                     ▼
       Object Detection Evaluation
```

---

## 🚦 Object Classes

The current baseline focuses on five selected object categories:

| Class ID | Object |
| :------: | ------ |
|     0    | Person |
|     1    | Car    |
|     2    | Truck  |
|     3    | Bus    |
|     4    | Bike   |

These classes were selected from the available BDD100K object categories for the current implementation.

---

## 🛠️ Technologies Used

| Technology      | Purpose                                        |
| --------------- | ---------------------------------------------- |
| **Python**      | Project implementation                         |
| **YOLOv8**      | Object detection model                         |
| **Ultralytics** | YOLO training and inference framework          |
| **OpenCV**      | Image processing and image-size extraction     |
| **tqdm**        | Progress tracking during annotation conversion |
| **BDD100K**     | Driving-scene dataset                          |

---

## 📁 Project Structure

```text
Low-Visibility-Object-Detection/
│
├── configs/
│   └── data.yaml
│
├── models/
│
├── notebooks/
│
├── scripts/
│   ├── convert_bdd_to_yolo.py
│   └── train.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

### Directory Description

**`configs/`**

Contains dataset and training configuration files.

**`models/`**

Used locally for model weights. Large model files are excluded from Git tracking.

**`notebooks/`**

Reserved for exploratory data analysis, experiments, visualization, and future model analysis.

**`scripts/`**

Contains the main Python scripts for dataset conversion and model training.

---

# 📊 Dataset

## BDD100K

This project uses the **BDD100K** dataset, a large-scale driving dataset containing diverse road scenes and annotations.

The dataset is **not included in this repository** because of its size and dataset distribution considerations.

After obtaining the dataset, the expected local structure is:

```text
Low-Visibility-Object-Detection/
│
├── datasets/
│   └── BDD100K/
│       ├── labels/
│       │   ├── bdd100k_labels_images_train.json
│       │   └── bdd100k_labels_images_val.json
│       │
│       ├── train/
│       │   ├── images/
│       │   └── labels/
│       │
│       └── val/
│           ├── images/
│           └── labels/
│
└── ...
```

The `datasets/` directory is excluded through `.gitignore`.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone git@github.com:rohanandelkar/low-visibility-object-detection.git
cd low-visibility-object-detection
```

## 2. Create a Virtual Environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔄 Dataset Preparation

Once BDD100K is placed in the expected `datasets/BDD100K/` directory, run:

```bash
python scripts/convert_bdd_to_yolo.py
```

The conversion script:

1. Reads the original BDD100K JSON annotations.
2. Identifies the selected object categories.
3. Reads the corresponding image dimensions.
4. Converts bounding boxes into YOLO format.
5. Generates `.txt` annotation files.
6. Stores the converted labels alongside the dataset.

### YOLO Annotation Format

Each object is stored as:

```text
class_id x_center y_center width height
```

All bounding-box coordinates are normalized between `0` and `1`.

---

# 🏋️ Model Training

The baseline model uses **YOLOv8 Nano (YOLOv8n)**.

Training can be started using:

```bash
python scripts/train.py
```

Current baseline configuration:

| Parameter  | Value          |
| ---------- | -------------- |
| Model      | YOLOv8n        |
| Epochs     | 50             |
| Classes    | 5              |
| Batch Size | Auto           |
| Dataset    | BDD100K subset |

The YOLOv8n pretrained weights are automatically obtained by Ultralytics when required and are intentionally excluded from Git tracking.

---

# 📈 Evaluation

Model performance should be evaluated using standard object-detection metrics such as:

* **Precision**
* **Recall**
* **mAP@50**
* **mAP@50–95**
* **F1-score**
* **Inference speed / FPS**

Future experiments will compare the baseline model against enhanced versions of the detection pipeline.

---

# 🌫️ Low-Visibility Enhancement — Future Direction

The current implementation establishes the baseline detection pipeline.

The next development stage will investigate methods for improving detection under challenging visibility conditions.

### Planned improvements

#### 1. Image Processing

Investigate preprocessing techniques such as:

* Contrast enhancement
* CLAHE
* Gamma correction
* Denoising
* Sharpening
* Dehazing
* Low-light enhancement

#### 2. Data Augmentation

Introduce realistic visibility degradation and environmental variations:

```text
Normal Images
     │
     ├── Fog
     ├── Rain
     ├── Haze
     ├── Low Light
     ├── Blur
     ├── Noise
     └── Contrast Variation
             │
             ▼
       Augmented Dataset
```

#### 3. Model Improvement

Potential areas of investigation include:

* Transfer learning
* Hyperparameter optimization
* Different YOLO architectures
* Improved feature extraction
* Attention mechanisms
* Multi-scale detection
* Model fine-tuning

#### 4. Generalization

The ultimate goal is to improve the model's ability to detect road objects across different:

* Visibility conditions
* Weather conditions
* Lighting conditions
* Camera environments
* Driving scenarios

---

# 🔬 Planned Experimental Pipeline

The project can eventually evolve into the following experimental framework:

```text
                    BDD100K
                       │
                       ▼
                Dataset Preparation
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Baseline Data       Enhanced Data
             │                   │
             ▼                   ▼
          YOLOv8n             YOLOv8n
             │                   │
             ▼                   ▼
       Baseline Model       Improved Model
             │                   │
             └─────────┬─────────┘
                       ▼
                 Performance
                  Comparison
                       │
                       ▼
             Generalization Analysis
```

This experimental design will allow quantitative comparison between the original baseline and the proposed improvements.

---

# 📌 Current Project Status

### Phase 1 — Baseline Pipeline

* [x] Project structure
* [x] BDD100K annotation conversion script
* [x] YOLO dataset configuration
* [x] YOLOv8 training script
* [x] Python dependency configuration
* [x] GitHub repository setup
* [ ] Baseline training evaluation
* [ ] Quantitative performance analysis
* [ ] Low-visibility augmentation
* [ ] Image enhancement experiments
* [ ] Improved model training
* [ ] Baseline vs improved-model comparison

---

# 🚀 Future Scope

The project is intended to evolve from a basic object-detection pipeline into a more robust **low-visibility object-detection system**.

Future work may include:

* Realistic synthetic fog and rain generation
* Low-light image enhancement
* Domain-specific augmentation
* Automated image-quality assessment
* Robust feature extraction
* Model architecture comparison
* Hyperparameter optimization
* Cross-condition evaluation
* Real-time inference
* Edge-device deployment
* Integration with ADAS-style applications

---

# 👨‍💻 Author

**Rohan Andelkar**

B.Tech — Computer Science / Engineering

GitHub: [@rohanandelkar](https://github.com/rohanandelkar)

---

# 📚 References

* BDD100K Dataset — Berkeley DeepDrive
* Ultralytics YOLO Documentation
* OpenCV Documentation

---

## ⭐ Project Vision

> **From baseline object detection to robust perception in challenging visibility conditions.**

This repository represents the baseline implementation and will serve as the foundation for further experimentation and development.
