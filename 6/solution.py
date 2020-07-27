import os
import re
import zipfile


file_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../6"))
file_path = file_path + "/"
file_name = file_path + "90052.txt"

zip_file = file_path + "channel.zip"
archive = zipfile.ZipFile(zip_file, "r")
comments = ''

def iterate_file(file_name):
    global comments
    while True:
        with open(file_name) as infile:
            data = infile.read()
        print(data)
        file_name = re.findall(r'Next nothing is (\d+)', data)
        if file_name:
            print(type(file_name[0]))
            comments += archive.getinfo(file_name[0]+".txt").comment.decode()
            file_name = file_path+file_name[0]+".txt"
        else:
            break


iterate_file(file_name)
print(comments)