import xmlrpc.client
uri = "http://www.pythonchallenge.com/pc/phonebook.php"
response = xmlrpc.client.ServerProxy(uri)
# phone = response.system.methodSignature('phone')
print(response.phone("Bert"))


# URL AFTER 8 http://www.pythonchallenge.com/pc/return/