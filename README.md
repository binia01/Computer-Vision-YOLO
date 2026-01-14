# PPE Safety Detection App

This project is a Computer Vision application built with [Streamlit](https://streamlit.io/) and [Ultralytics YOLO](https://github.com/ultralytics/ultralytics). It detects Personal Protective Equipment (PPE) such as hard hats and safety vests in uploaded images.

## Features

- **Upload Image**: Support for JPG, PNG, and JPEG formats.
- **Object Detection**: Uses a trained YOLO model to identify safety gear.
- **Visualization**: Displays the original image and the detection results with bounding boxes.
- **Count Summary**: Provides a quick count of detected objects.

## Prerequisites

- Python 3.8+
- A trained YOLO model file named `best.pt` placed in the data directory.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Computer-Vision-YOLO
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Important**: Ensure you have your trained `./data/best.pt` model file in the project directory.

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser to the local URL provided (usually `http://localhost:8501`).

## Dependencies

- streamlit
- ultralytics
- pillow
- numpy
