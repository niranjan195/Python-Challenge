import os
import re
from PIL import Image


sol_no = re.findall('(\d+).py', __file__)[0]
file_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../%s" % sol_no))
file_name = file_path + '/wire.png'

img = Image.open(file_name)
width, height = img.size
pixels = img.load()

new_img = Image.new("RGB", (100, 100))
result_pixel = new_img.load()
'''
1+2+3+...+n = (n*(n-1))/2
2(1+2+3+...+n) = n*(n-1)
2(1+2+3+...+n) = n*n - n
2(1+2+3+...+(n-1) + n = n*n
2(100+99+99+98+98+97+97....) = 100*100
'''
steps_list = [100-1]
for i in range(99):
    steps_list.append(99-i)
    steps_list.append(99-i)

print(steps_list)


direction = ['r', 'd', 'l', 'u']
location = [0, 0]
in_wid = 0


def get_new_location(location, direction):
    new_location = location
    if direction == "r":
        new_location[0] += 1
    elif direction == "d":
        new_location[1] += 1
    elif direction == "u":
        new_location[1] -= 1
    elif direction == "l":
        new_location[0] -= 1
    return new_location


for i in range(len(steps_list)):
    cur_direction = direction[i % len(direction)]
    for j in range(steps_list[i]):
        result_pixel[location[0], location[1]] = pixels[in_wid, 0]
        # print(location[0],location[1])
        in_wid += 1
        location = get_new_location(location, cur_direction)
new_img.save(file_path + "/result.jpg")
