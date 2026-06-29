# 🚀 Real-Time Object Detection and Tracking using YOLOv8

## 📌 Overview

This project is a real-time object detection and tracking application built with **Python**, **YOLOv8**, **OpenCV**, and a custom **SORT tracker**. The application captures live video from a webcam, detects objects using the YOLOv8 model, and assigns a unique tracking ID to each detected object.

This project demonstrates the fundamentals of computer vision, object detection, and multi-object tracking.

---

## ✨ Features

* 🎥 Real-time webcam object detection
* 📦 YOLOv8 object detection model
* 🔍 Multi-object tracking using a custom SORT tracker
* 🆔 Unique ID assignment for detected objects
* 📐 Bounding boxes with corner styling using CVZone
* ⚡ Fast and lightweight implementation

---

## 🛠 Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy
* CVZone

---

## 📂 Project Structure

```text
Object-Detection-and-Tracking/
│
├── main.py
├── sort.py
├── coco.txt
├── yolov8n.pt
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
    └── output.png
```

---

## 📋 Detected Objects

The project is configured to detect objects from the COCO dataset, including:

* Person
* Bicycle
* Car
* Motorcycle
* Bus
* Truck
* Dog
* Cat
* Kerchief (if included in your custom class file)

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Object-Detection-and-Tracking.git
```

### 2. Navigate to the project folder

```bash
cd Object-Detection-and-Tracking
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Download the YOLOv8 model

Place the **yolov8n.pt** model file in the project folder.

### 5. Run the application

```bash
python main.py
```

---

## 📷 Output

The program opens the webcam and:

* Detects objects in real time
* Draws bounding boxes around detected objects
* Assigns a unique tracking ID to each object
* Displays the processed video stream

Press **Q** to exit the application.

---

## 📸 Screenshot

Add screenshots inside the **screenshots** folder.

Example:

```text
screenshots/output.png
```

---

## 🚀 Future Improvements

* Object counting
* Vehicle counting
* Line crossing detection
* Speed estimation
* Face recognition
* Custom YOLO model training
* Video file input support
* Save processed output video
* GPU acceleration
* Improved SORT tracking algorithm

---

## 💡 Applications

* Smart surveillance
* Traffic monitoring
* Vehicle tracking
* Retail analytics
* Smart city systems
* Security monitoring
* Autonomous robotics

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, improve the project, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Joseph Frenodas**

Electronics and Communication Engineering (ECE) Student

AI | Computer Vision | Machine Learning Enthusiast

⭐ If you found this project useful, please consider giving it a Star!
