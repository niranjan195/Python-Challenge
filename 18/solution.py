import os
import re
import gzip
import difflib


sol_no = re.findall(r'(\d+).py', __file__)[0]
file_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../%s" % sol_no))
file_name = file_path + "/deltas.gz"

data = gzip.open(file_name)


ls,rs = [],[]

for line in data:
    ls.append(line[:53].decode()+"\n")
    rs.append(line[56:].decode())

compare = difflib.Differ().compare(ls,rs)

space = open(file_path+ "/space.png", "wb")
plus = open(file_path+ "/plus.png", "wb")
minus = open(file_path+ "/minus.png", "wb")

for line in compare:
    seq = line[:2]
    byt = bytes([int(x,16) for x in line[2:].strip().split(" ") if x])
    print(byt)
    if seq == "+ ": plus.write(byt)
    elif seq == "- ": minus.write(byt)
    else: space.write(byt)

space.close()
plus.close()
minus.close()



s1 = ['1','2','3']
s2 = ['1','2','4']

compare = difflib.Differ().compare(s1,s2)
for line in compare:
    print(line)