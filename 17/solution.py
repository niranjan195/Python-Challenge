import re
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
import bz2
import xmlrpc.client

# Read level4 cookie
def read_cookie(url):
    level4_url = url
    resp = urlopen(level4_url)
    cookie = resp.getheader('Set-Cookie')
    info = re.match('info=(.*?);', cookie).group(1)
    return info


# Follow new url
busy_nothing = "12345"
def repeated_traverse(busy_nothing):
    global cookies
    while True:
        level4_modified_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s" % busy_nothing
        try:
            data = urlopen(level4_modified_url).read().decode()
            cookie_info = read_cookie(level4_modified_url)
        except BaseException:
            print('TIMED-OUT-COOKIES', cookies)
            return
        cookies.append(cookie_info)
        print(data)
        busy_nothing = re.findall(r'and the next busynothing is (\d+)', data)
        if busy_nothing:
            busy_nothing = busy_nothing[0]
        else:
            print(level4_modified_url)
            return level4_modified_url


level4_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
# info=read_cookie(level4_url)

cookies = []
# final_level_4_modified_url = repeated_traverse(busy_nothing)


cookie_string = b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'

decompressed_cookie_string = bz2.decompress(cookie_string)
print(decompressed_cookie_string)


# level15-MOZARTS FATHER LEOPOLD
# LEVEL 13 PHONEBOOK TO CALL
uri = "http://www.pythonchallenge.com/pc/phonebook.php"
response = xmlrpc.client.ServerProxy(uri)
# phone = response.system.methodSignature('phone')
print(response.phone("Leopold"))


#Send the message
msg = "the flowers are on their way"
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
req = Request(url,headers={"Cookie": "info=" + quote_plus(msg)})
print(urlopen(req).read().decode())