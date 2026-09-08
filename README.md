# Low-Visibility Object Detection

A computer vision project for detecting objects in low-visibility driving conditions using the BDD100K dataset and YOLO object detection.

## Overview

Object detection in low-visibility environments such as fog, rain, haze, and poor lighting is challenging because reduced visibility can affect object appearance, contrast, and detection accuracy.

This project explores an object detection pipeline using the BDD100K driving dataset and YOLO. The project focuses on converting BDD100K annotations into YOLO format and training a YOLOv8 model on selected object classes.

## Objectives

- Convert BDD100K annotations into YOLO format.
- Prepare the dataset for YOLO-based object detection.
- Train a YOLOv8 model on selected object categories.
- Establish a baseline for object detection under challenging visibility conditions.
- Provide a foundation for future improvements using image processing, augmentation, and model optimization.

## Classes

The current implementation focuses on five object classes:

| ID | Class |
|----|-------|
| 0 | Person |
| 1 | Car |
| 2 | Truck |
| 3 | Bus |
| 4 | Bike |

## Project Structure

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
