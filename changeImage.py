#!/usr/bin/env python3
import glob
import os
from PIL import Image

def changeImage(source_path, dest_path):
    print(source_path, dest_path)
    with Image.open(source_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        try:
            new_path = os.path.splitext(dest_path)[0] + '.jpeg'
            print('new', new_path)
            img.save(new_path, "JPEG")
            print('img modified and saved to:', new_path)
        except OSError:
            print('cannot save file', OSError)

paths = glob.glob("*/*.tiff", recursive=True)
for path in paths:
    changeImage(path, path)
