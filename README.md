# License Plate Recognition (LPR) System

A robust Python-based system designed to detect and recognize vehicle license plates from images using **Computer Vision** and **Optical Character Recognition (OCR)**.

## Key Features
* **Plate Detection:** High-accuracy contour analysis and morphological operations to locate plates.
* **Image Pre-processing:** Advanced filtering (Bilateral Filter), Grayscale conversion, and Canny Edge detection.
* **OCR Integration:** Extracts text from the detected plate region using machine learning models.
* **Performance:** Optimized image processing pipeline for clear character extraction even in varying light conditions.

## Tech Stack
* **Python 3.x**
* **Matplotlib:** Visualization of results.
* **Scikit Image:** For image processes

## Demo Results
> [Insert a screenshot or a GIF of your project in action here!]
> Example: `![Result](./output_example.png)`

##  Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/UmutAA/license-plate-recognition.git](https://github.com/UmutAA/license-plate-recognition.git)
   cd your-repo-name
   ```
2. **Activate Virtual Environment:**
   Windows:
   ```bash
   cd lpr\Scripts\activate
   ```

   Linux/macOS: 
   ```bash
   source lpr/bin/activate   
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application:**
   ```bash
   python main.py
   ```
