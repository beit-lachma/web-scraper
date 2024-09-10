try:
    from urllib.parse import urlparse, urlunparse  # Py 3
except ImportError:
    from urlparse import urlparse, urlunparse  # Py2

# Parse a URL
parsed_url = urlparse(
    'https://github.com/beit-lachma')
print(parsed_url)
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.params)
print(parsed_url.query)
print(parsed_url.fragment)

# Create a URL
new_url = urlunparse(
    ('https',               # Scheme
     'https://github.com',  # Netloc
     '/beit-lachma',            # Path
     None,                  # Params
     'q=5&x=that',          # Query (use urlencode())
     'test_fragment'))      # Fragment
print(new_url)