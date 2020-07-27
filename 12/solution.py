import os

file_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../12"))
file_name = file_path + "/evil2.gfx"

with open(file_name, 'rb') as infile:
    data = infile.read()

img_ext = ['jpg','png','gif','png','jpg']

for i in range(5):
    img_file = file_path+"/%d." % (i)+img_ext[i]
    print(img_file)
    with open(img_file, 'wb') as outfile:
        outfile.write(data[i::5])