from PIL import Image
import os

parent = os.getcwd()

IN_PATH = f"{parent}/input/"
OUT_PATH = f"{parent}/output/"
NAME = ""

new_size = (540, 640)


i = 1
limit = 60
while i < limit:
    image = Image.open(f"{IN_PATH}{i}.png")
    resize_img = image.resize(new_size, Image.Resampling.LANCZOS)
    resize_img.save(f"{OUT_PATH}{i}.png")
    i += 1
