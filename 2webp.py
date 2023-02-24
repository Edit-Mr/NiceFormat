import sys
import os
from PIL import Image

# Get the paths of the dragged files
paths = sys.argv[1:]

for path in paths:
    # Open the image and convert it to WebP format
    with Image.open(path) as img:
        output_path = os.path.splitext(path)[0] + ".webp"
        img.save(output_path, "webp")