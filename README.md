# Dynamic Background Removal

## Description
This project demonstrates dynamic background removal using chroma keying techniques with OpenCV. It processes a video with a green screen background and replaces it with a different background image.

## Features
- **Chroma Keying:** Removes green screen backgrounds from videos.
- **Background Replacement:** Allows you to insert any image as the new background.
- **Real-Time Display:** Optionally displays the processed video in real-time.
- **Command-Line Interface:** Easy-to-use command-line arguments for customization.

## Requirements
- Python 3.6 or higher
- OpenCV
- NumPy

## Usage
### Prepare Your Assets
Input Video: Ensure your input video has a solid green background (chroma key).
Background Image: Choose an image to replace the green background.

### Run the script

```
python background_removal.py --video path/to/input_video.mp4 --background path/to/new_background.jpg --output path/to/output_video.mp4
```

Example:
```
python background_removal.py --video input_video.mp4 --background new_background.jpg --output output_video.mp4
```

The script will display the processed video in a window. Press q to quit the display window.


