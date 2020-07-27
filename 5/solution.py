import urllib.request
import pickle

# url = "http://www.pythonchallenge.com/pc/def/banner.p"
# data = urllib.request.urlopen(url).read().decode()
# Data has been written to 5.txt file

with open("5/5.txt") as infile:
    data = infile.read().encode()

deserialized_data = pickle.loads(data)

for l in deserialized_data:
    print(''.join([k*v for k, v in l]))
