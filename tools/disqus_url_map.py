from urllib.parse import urlparse
import os

with open('thephysicsvirtuosi-2019-01-24T07_53_39.291678-links.csv', 'r') as f, open('urlmap.csv', 'w') as g:
    for line in f:

        starting_url = line.strip()

        g.write(starting_url)
        g.write(', ') 

        url = urlparse(starting_url)

        shortname = os.path.splitext(os.path.basename(url.path))[0]

        g.write('https://thephysicsvirtuosi.com/posts/old/' + shortname + '/')
        g.write('\n')


