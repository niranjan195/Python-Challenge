import urllib.request
import re


FINAL_SOLUTION = "peak.html"

# start_nothing = "12345"
nothing = "66831"
def repeated_traverse(nothing):
    while True:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % (nothing)
        data = urllib.request.urlopen(url).read().decode()
        print(data)
        nothing = re.findall(r'and the next nothing is (\d+)',data)
        if nothing:
            nothing = nothing[0]
        else:
            print(url)
            return data

data = repeated_traverse(nothing)
# nothing = "94485"
# data = repeated_traverse(nothing)
# print(data)
# nothing = str(16044//2)
# data = repeated_traverse(nothing)
# print(data)

