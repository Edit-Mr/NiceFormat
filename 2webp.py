import sys
import os
from PIL import Image

# Get the paths of the dragged files
paths = sys.argv[1:]

for path in paths:
    # Get the file extension
    extension = os.path.splitext(path)[1].lower()

    # Check the file extension and perform the appropriate conversion
    if extension == ".webp":
        # Convert WebP to PNG
        with Image.open(path) as img:
            output_path = os.path.splitext(path)[0] + ".png"
            img.save(output_path, "png")
    elif extension == ".webm":
        # Convert WebM to MP4
        output_path = os.path.splitext(path)[0] + ".mp4"
        # Your code for converting WebM to MP4 goes here
        # ...
    else:
        print(f"Unsupported file format: {extension}")
