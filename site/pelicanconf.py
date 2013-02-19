#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'The Virtuosi'
SITENAME = u'The Virtuosi'
SITEURL = ''
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
