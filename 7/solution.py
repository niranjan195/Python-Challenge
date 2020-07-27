import os
import re
from PIL import Image


file_name = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../7/oxygen.png"))
img = Image.open(file_name)

center_height = img.height//2
gray_pixels = [img.getpixel((x, center_height)) for x in range(img.width)]
duplicates_removed_gray_pixels = gray_pixels[::7]
pixels_without_noise = [r for r, g, b,
                            a in duplicates_removed_gray_pixels if r == g == b]
# print(pixels_without_noise)
# string = "".join(chr(c) for c in pixels_without_noise)
string = "".join(map(chr,pixels_without_noise))
print(string)
numbers = re.findall(r'\d+',string)
print(numbers)
string = "".join(map(chr,map(int,numbers)))
print(string)
# print('\n'.join(dir(img)))
# print(help(img.getpixel))
