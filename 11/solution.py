# See even jpg file

import os
from PIL import Image, ImageDraw


file_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../11"))
file_name = file_path + "/cave.jpg"
img = Image.open(file_name)

size = (img.width,img.height)

even = Image.new("RGB",size)
odd = Image.new("RGB",size)


for row in range(img.width):
    for col in range(img.height):
        pi = img.getpixel((row,col))
        if (row + col) % 2 == 0:
            even.putpixel((row,col),pi)
        else:
            odd.putpixel((row,col),pi)


even.save(file_path + "/even.jpg")
odd.save(file_path + "/odd.jpg")
