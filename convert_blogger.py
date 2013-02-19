"""
File to convert our old blog from atom format to Markdown
"""

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
from html2text import html2text

# load xml dump as tree
with open(FILE) as f:
    tree = etree.parse(f,base_url='http://www.w3.org/2005/Atom')
    root = tree.getroot()

# template for post
md_template = u"""Title: {title}
Date: {date}
Tags: {tags}
Category: old
Slug: {slug}
Author: {author}

{content}
"""
# note: missing summary and tags

# get all of the entries
entries = root.findall(begin+'entry')
# includes all comments and junk, must filter
posts = [ z for z in entries if any('post' in x.get('term') for x in z.findall(begin+'category')) ]
# posts = [ z for z in entries if z.find('{http://purl.org/syndication/thread/1.0}in-reply-to') is not None and z.find('{http://purl.org/syndication/thread/1.0}in-reply-to') is not None ]

# custom namedtuple
post_tuple = namedtuple('post','title author date slug tags content')

def process_post(post):
    title = post.find(begin+'title').text
    author = post.find(begin+'author').find(begin+'name').text
    date = datetime.strftime(dateutil.parser.parse(post.find(begin+'published').text),'%Y-%m-%d %H:%M:%S')
    try:
        slug = re.sub(r'\W+','-',unidecode(title.lower()))
    except AttributeError:
        slug = 'blank'
    tags = u", ".join( x.get('term') for x in post.findall(begin+'category') if 'post' not in x.get('term') )
    content = post.find(begin+'content').text

    # try to handle mathjax
    try:
        content = content.replace('&nbsp;',' ')
        content = content.replace('\]','$$')
        content = content.replace('\[','$$')
        content = content.replace('<br />','\n')
    except AttributeError:
        pass
    # try:
    #     content = html2text(content)
    # except AttributeError:
    #     pass
    try:
        content = content.replace('<br />','\n')
    except AttributeError:
        pass

    return post_tuple(title,author,date,slug,tags,content)

processed_posts = map(process_post, posts)
processed_posts = [ p for p in processed_posts if p.title ]


if __name__ == "__main__":
    for pp in processed_posts:
        print "Converting: ", pp.title
        with open(os.path.join(OUTPUT_DIR,pp.slug+'.md'),'w') as f:
            body =  md_template.format(**pp._asdict())
            f.write(body.encode('utf-8'))



