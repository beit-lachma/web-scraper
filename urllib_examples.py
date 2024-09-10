# HTTP GET and POST requests with standard library
try:
    # Python 3
    from urllib.request import urlopen, Request
except:
    # Python 2
    from urllib2 import urlopen, Request


# Open URL with string
response = urlopen('https://github.com/beit-lachma')
print(response.read())

print('------------------------------------------')

# Or prebuild the request
request = Request('https://github.com/beit-lachma')
request.add_header('User-Agent', 'Not Firefox')
response = urlopen(request)
print(response.read())
