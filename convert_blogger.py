from __future__ import unicode_literals

FILE = 'blogger-backup-blog-02-19-2013.xml'
begin = '{http://www.w3.org/2005/Atom}'
OUTPUT_DIR='old-content'

from lxml import etree
import re, os
from collections import namedtuple
from unidecode import unidecode
import dateutil.parser
from datetime import datetime

with open(FILE) as f:
    tree = etree.parse(f,base_url='http://www.w3.org/2005/Atom')
    root = tree.getroot()

md_template = u"""Title: {title}
Date: {date}
Tags: {tags}
Category: old
Slug: {slug}
Author: {author}

{content}
"""
# note: missing summary and tags

entries = root.findall(begin+'entry')
posts = [ z for z in entries if any('post' in x.get('term') for x in z.findall(begin+'category')) ]
# posts = [ z for z in entries if z.find('{http://purl.org/syndication/thread/1.0}in-reply-to') is not None and z.find('{http://purl.org/syndication/thread/1.0}in-reply-to') is not None ]

post_tuple = namedtuple('post','title author date slug tags content')

def process_post(post):
    title = post.find(begin+'title').text
    author = post.find(begin+'author').find(begin+'name').text
    date = datetime.strftime(dateutil.parser.parse(post.find(begin+'published').text),'%Y-%m-%d %H:%M:%S')
    if title:
        slug = re.sub(r'\W+','-',unidecode(title.lower()))
    else:
        slug = 'blank'
    tags = u", ".join( x.get('term') for x in post.findall(begin+'category') if 'post' not in x.get('term') )
    content = post.find(begin+'content').text

    return post_tuple(title,author,date,slug,tags,content)

processed_posts = map(process_post, posts)
processed_posts = [ p for p in processed_posts if p.title ]


if __name__ == "__main__":
    for pp in processed_posts:
        print "Converting: ", pp.title
        with open(os.path.join(OUTPUT_DIR,pp.slug+'.md'),'w') as f:
            body =  md_template.format(**pp._asdict())
            f.write(body.encode('utf-8'))



