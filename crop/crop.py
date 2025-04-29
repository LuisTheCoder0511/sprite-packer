from PIL import Image
import os

parent = os.getcwd()

IN_PATH = f"{parent}/input/"
OUT_PATH = f"{parent}/output/"
NAME = ""

x=58
y=1024 - 58
w=608
h=521

i = 1
while i <= 19:
    image = Image.open(f"{IN_PATH}{NAME}{i}.png")
    crop = image.crop((x, y - h, x + w, y))
    crop.save(f"{OUT_PATH}{i}.png")
    i+=1
