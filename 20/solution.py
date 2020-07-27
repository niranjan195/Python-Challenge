from urllib.request import Request, urlopen
import base64
import os
import re

sol_no = re.findall('(\d+).py', __file__)[0]
file_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../%s" % sol_no))
file_name = file_path + '/res.txt'

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
req = Request(url)
cred = base64.b64encode(b"butter:fly")
req.add_header("Authorization", "Basic %s" % cred.decode())

res = urlopen(req)
headers = res.headers
pattern = re.compile("bytes (\d+)-(\d+)/(\d+)")
content_range = headers['Content-Range']
start, end, total = pattern.search(content_range).groups()
req.headers['Range'] = 'bytes=%i-' % (int(end)+1)


def read_remaining_data():
    while True:
        try:
            res = urlopen(req)
            headers = res.headers
            # print("HEADERS", headers)
            print('Message: ',res.read().decode())
            content_range = headers['Content-Range']
            start, end, total = pattern.search(content_range).groups()
            req.headers['Range'] = 'bytes=%i-' % (int(end)+1)
        except:
            print(content_range)
            print("Breaking")
            break

# read_remaining_data()

# last content-range: bytes 30313-30346/2123456789
req.headers['Range'] = 'bytes=2123456790-'
res = urlopen(req)
# print(res.headers)
password_hint = res.read().decode()[::-1]

req.headers['Range'] = 'bytes=2123456743-'
res = urlopen(req)
# print(res.headers)
zip_number = re.match('and it is hiding at (\d+)',res.read().decode()).group(1)

req.headers['Range'] = 'bytes=%s-' % zip_number
res = urlopen(req)
# print(res.headers)

zip_file = file_path + '/solution.zip'

with open(zip_file, 'wb') as zipfile:
    zipfile.write(res.read())

print("Final password: ", 'invader'[::-1])