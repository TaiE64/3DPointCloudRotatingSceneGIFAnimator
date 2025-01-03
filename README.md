
# PlyToGifPipeline

A Python-based pipeline to convert `.ply` point cloud files into `.mp4` videos and then further into `.gif` animations. This repository automates the process, making it easy to create visual representations of 3D data for various purposes like presentations and visual analyses.

## Features
- Convert `.ply` point cloud files to `.mp4` videos with adjustable resolution and frame rate.
- Generate `.gif` animations from `.mp4` files using FFmpeg.
- Fully customizable pipeline.

## Installation
### Prerequisites
1. Python 3.7 or higher
2. Required Python libraries:
   - `open3d`
   - `numpy`
   - `opencv-python`
   - `ffmpeg` (external dependency)

Install the required Python packages using pip:
```bash
pip install open3d numpy opencv-python
```

Ensure FFmpeg is installed on your system. For installation instructions, visit [FFmpeg Installation Guide](https://ffmpeg.org/download.html).

## Usage

### 1. Prepare Directories
- Place your `.ply` files in a folder (e.g., `ply_test`).
- Create output folders named `mp4` and `gif`.

### 2. Run the Pipeline
Execute the script `RUN.py`:
```bash
python RUN.py
```

### 3. Output
- The `.mp4` files will be saved in the `mp4` folder.
- The `.gif` files will be saved in the `gif` folder.

## Code Overview

### `ply_to_mp4.py`
This script converts `.ply` files to `.mp4` videos. It uses Open3D for rendering and OpenCV for video encoding.

### `mp4_to_gif.py`
This script converts `.mp4` files into `.gif` animations using FFmpeg.

### `RUN.py`
This is the main script that orchestrates the entire pipeline by invoking the above two modules.

## Example
Given a `.ply` file named `example.ply`:
1. The script will generate `example.mp4` in the `mp4` folder.
2. Then, it will create `example.gif` in the `gif` folder.

## Contributing
Feel free to fork the repository and submit pull requests. Suggestions and improvements are always welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy converting!
