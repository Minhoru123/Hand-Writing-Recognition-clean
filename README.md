# Hand-Writing-Recognition

A handwriting recognition project using OCR and deep learning techniques to analyze and recognize handwritten names from a large dataset.

### Project Overview

This project focuses on handwriting recognition using a dataset of over 400,000 handwritten names collected through charity projects. The goal is to develop a model that can accurately recognize and digitize handwritten text.

### Dataset

Dataset location: https://www.kaggle.com/datasets/landlord/handwriting-recognition

The dataset includes:
**-** 206,799 first names
**-** 207,024 surnames
**-** Split into:
**-** Training set (331,059 samples)
**-** Testing set (41,382 samples)
**-** Validation set (41,382 samples)

### Prerequisites

* Python 3.x
* Git
* pip (Python package installer)
* PyTorch
* OpenCV (cv2)

## Installation

1. Clone the repository

```
git clone https://github.com/Minhoru123/Hand-Writing-Recognition.git
cd Hand-Writing-Recognition
```

2. Create virtual environment

   ```
   python -m venv myenv
   ```
3. Activate the virtual environment

* Windows:

  ```
  myenv\Scripts\activate
  ```
* macOS/Linux:

  ```
  source myenv/bin/activate
  ```

4. Install required packages

   ```
   pip install -r requirements.txt
   ```

### Important Note About Large Files

This project uses some large model files and libraries. Due to GitHub's file size limitations, these files are not directly included in the repository. The following files need to be handled separately:

* `myenv/Lib/site-packages/cv2/cv2.pyd` (71 MB)
* `myenv/Lib/site-packages/torch/lib/torch_cpu.dll` (237.76 MB)
* `myenv/Lib/site-packages/torch/lib/dnnl.lib` (623.27 MB)

These files will be automatically installed when you run `pip install -r requirements.txt`.

## Features

* Handwriting recognition and digitization
* Support for various handwriting styles
* [Add other key features of your project]

## Contributing

1. Fork the repository
2. Create your feature branch

   ```
   git checkout -b feature/YourFeature
   ```
3. Commit your changes

   ```
   git commit -m 'Add some feature'
   ```
4. Push to the branch

   ```
   git push origin feature/YourFeature
   ```
5. Open a Pull Request

   ```
   git push origin feature/YourFeature
   ```
