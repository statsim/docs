#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anton Zemlyansky'
SITENAME = u'StatSim Documentation'
SITEURL = ''
LOCALE = 'en_US.UTF-8'

PATH = 'content'
OUTPUT_PATH = 'docs'

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
PLUGINS = ['i18n_subsites', 'ipynb.markup']
I18N_SUBSITES = {
  'ru': {
    'SITENAME': 'Справочник StatSim'
  }
}
THEME = 'themes/pelican-blue'
DISPLAY_FOOTER = False
DISPLAY_SUMMARY = True
ARTICLE_ORDER_BY = 'filename'
DEFAULT_PAGINATION = False

DELETE_OUTPUT_DIRECTORY = True
IGNORE_FILES = ['*-checkpoint.ipynb', '*.md', '*.html']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
