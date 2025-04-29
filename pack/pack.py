from PIL import Image
import os

parent = os.getcwd()

IN_PATH = f"{parent}/input/"
OUT_PATH = f"{parent}/output/"

limit = 13
i = 1
j = 1
IMG_WIDTH = 94
IMG_HEIGHT = 526
WIDTH = IMG_WIDTH * limit + limit + 1
image = Image.new(mode="RGBA", size=[WIDTH, IMG_HEIGHT])

while i <= limit:
    load = Image.open(f"{IN_PATH}{i}.png")
    image.paste(load, (j, 0))
    i+=1
    j+=IMG_WIDTH + 1

image.show()
image.save(f"{OUT_PATH}Right.png")
