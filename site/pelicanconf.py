#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'The Virtuosi'
SITENAME = u'The Physics Virtuosi'
SITEURL = 'http://thephysicsvirtuosi.com'
TIMEZONE = "America/New_York"

DEFAULT_LANG = u'en'
DEFAULT_DATE='fs'
FALLBACK_ON_FS_DATE = True

# MD_EXTENSIONS = (['codehilite','mathjax'])

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Built on Facts', 'http://scienceblogs.com/builtonfacts/'),
        ('Uncertain Principles', 'http://scienceblogs.com/principles/'),
        ('Dot Physics', 'http://www.wired.com/wiredscience/'),
        ('Swans on Tea', 'http://blogs.scienceforums.net/swansont/'),
        )

# Social widget
SOCIAL = (('twitter','https://twitter.com/thevirtuosi'),
        ('facebook','https://www.facebook.com/thevirtuosi'),
        )

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

TWITTER_USERNAME = 'thevirtuosi'
GOOGLE_ANALYTICS = 'UA-15719155-6'
DISQUS_SITENAME = 'thephysicsvirtuosi'

FILES_TO_COPY = ( ('../extra/CNAME','CNAME' ), )

