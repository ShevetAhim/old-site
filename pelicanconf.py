#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Gurion'
SITENAME = u'Galilee Bedouin Camplodge'
SITEURL = ''
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

# Keywords and metadata
DESCRIPTION = 'Naturally slow down in the Bedouin village of Tabash. unique experience guaranteed!'
KEYWORDS = ('bedouin hospitality', 'camplodge', 'galilee', 'tent', 'hostel')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Add the accomodations page to those rendered without content
DIRECT_TEMPLATES = ['index', 'archives', 'accomodations', 'email_sent']

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SIDEBAR = True
BOOTSTRAP_THEME = 'readable-old'
SHOW_ARTICLE_AUTHOR = True

STATIC_PATHS = [
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Plugins
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'pages': .8,
    },
}
