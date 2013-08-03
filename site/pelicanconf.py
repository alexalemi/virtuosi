#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'The Virtuosi'
SITENAME = u'The Physics Virtuosi'
SITEURL = 'http://localhost:8000'
TIMEZONE = "America/New_York"

DEFAULT_LANG = u'en'
DEFAULT_DATE='fs'
FALLBACK_ON_FS_DATE = True

MD_EXTENSIONS = ['extra','mathjax']

FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
GITHUB_URL = "http://github.com/alexalemi/virtuosi/"
GITHUB_POSITION = 'right'

STATIC_PATHS = ["images","static",]
PATH = "content"
PAGE_DIR = 'pages'
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS =  (('Built on Facts', 'http://scienceblogs.com/builtonfacts/'),
        ('Uncertain Principles', 'http://scienceblogs.com/principles/'),
        ('Dot Physics', 'http://www.wired.com/wiredscience/'),
        ('Swans on Tea', 'http://blogs.scienceforums.net/swansont/'),
        ('Old Virtuosi', 'http://thevirtuosi.blogspot.com'),
        )

# Social widget
SOCIAL = (('twitter','https://twitter.com/thevirtuosi'),
        ('facebook','https://www.facebook.com/thevirtuosi'),
        ('github', GITHUB_URL),
        ('rss', FEED_RSS),
        ('atom', FEED_ATOM),
        )


DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_EXCLUDES = ('drafts', 'oldhtml',)

TWITTER_USERNAME = 'thevirtuosi'
GOOGLE_ANALYTICS = 'UA-15719155-6'
DISQUS_SITENAME = 'thephysicsvirtuosi'
# GOOGLE_CUSTOM_SEARCH_SIDEBAR = '016118979984514975664:u9tdrwxiom8'

FILES_TO_COPY = ( ('extra/CNAME','CNAME' ), ('extra/.gitkeep', '.gitkeep' ) )

THEME = 'themes/justread'
# THEME_STATIC_PATHS = ['static','css','less']

TYPOGRIFY = True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50

SUMMARY_MAX_LENGTH = 150

PLUGIN_PATH = "pelican-plugins"
PLUGINS=['sitemap','gzip_cache','summary']

#plugin settings
SUMMARY_END_MARKER = "<!-- more -->"
SUMMARY_BEGIN_MARKER = "<!-- less -->"
# RESPONSIVE_FIGURES = True
SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.9,
            'indexes': 0.3,
            'pages': 0.3
            },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
            }
        }
