import sys
import os
from PIL import Image
paths = sys.argv[1:]
for path in paths:
    extension = os.path.splitext(path)[1].lower()
    # if file name is icon, covert to .ico
    if os.path.basename(path).lower() == "icon":
        with Image.open(path) as img:
            output_path = os.path.splitext(path)[0] + ".ico"
            img.save(output_path, "ico")
    elif extension == ".webp":
        # Convert WebP to PNG
        with Image.open(path) as img:
            output_path = os.path.splitext(path)[0] + ".png"
            img.save(output_path, "png")
    elif extension == ".jpg" or extension == ".jpeg" or extension == ".png" or extension == ".bmp" or extension == ".gif" or extension == ".tiff" or extension == ".tif":
        # Convert JPG or JPEG to WebP
        with Image.open(path) as img:
            output_path = os.path.splitext(path)[0] + ".webp"
            img.save(output_path, "webp")
    elif extension == ".heic":
        # Convert HEIC to JPG
        with Image.open(path) as img:
            output_path = os.path.splitext(path)[0] + ".jpg"
            img.save(output_path, "jpeg")
    elif extension == ".avif":
        # Convert AVIF to PNG
        with Image.open(path) as img:
            output_path = os.path.splitext(path)[0] + ".png"
            img.save(output_path, "png")
    else:
        print(f"Unsupported file format: {extension}")
