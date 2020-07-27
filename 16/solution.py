import os
import re
from PIL import Image, ImageChops

sol_no = re.findall('(\d+).py', __file__)[0]
file_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../%s" % sol_no))
file_name = file_path + "/mozart.gif"

gif = Image.open(file_name)


def draw_tmp_gif(index):
    tmp_gif = gif.copy()
    tmp_gif.frombytes(bytes([index] * (tmp_gif.height * tmp_gif.width)))
    tmp_gif.show()


max_pixel = max(enumerate(gif.histogram()), key=lambda x: x[1])
# draw_tmp_gif(max_pixel[0])

pink_pixel = [(i, pi) for i, pi in enumerate(gif.histogram())
              if pi % gif.height == 0 and pi != 0]

print(pink_pixel)
# draw_tmp_gif(pink_pixel[0][0])


# print(help(gif.crop))
# print("\n".join(dir(ImageChops)))
# print(help(ImageChops.offset))
for y in range(gif.height):
    box = 0, y, gif.width, y+1
    row = gif.crop(box)
    by = row.tobytes()
    pink_in_each_row = by.index(pink_pixel[0][0])
    row = ImageChops.offset(row, -pink_in_each_row)
    gif.paste(row, box)
gif.save(file_path+"/result.gif")
