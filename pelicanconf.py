#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anton Zemlyansky'
SITENAME = u'StatSim Documentation'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'
STATIC_PATHS = ['img']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('StatSim', 'https://statsim.com/'),
         ('Analyze.li', 'https://analyze.li'),
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/statsimcom'),
          ('Facebook', 'https://www.facebook.com/statsim'),
          ('Github', 'https://github.com/statsim'))

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = 'themes/pelican-blue'
DISPLAY_FOOTER = False
DISPLAY_SUMMARY = True
ARTICLE_ORDER_BY = 'filename'

DEFAULT_PAGINATION = False

IGNORE_FILES = ['*-checkpoint.ipynb', '*.md', '*.html']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
