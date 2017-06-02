#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jimmy Jiang'
SITENAME = "Jimmy's Lab"
SITEURL = ''
SITESUBTITLE = 'Algorihtm Engineer'
SITELOGO = '/extra/sitelogo.ico'
FAVICON = '/extra/sitelogo.ico'

PYGMENTS_STYLE = 'monokai'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

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

# Social widget
SOCIAL = ( ('github', 'https://github.com/jglwiz') )
          

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# plugin for jupyter notebook
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

STATIC_PATHS = ['images', 'extra']

DISQUS_SITENAME = 'jglwiz-blog'

# THEME
THEME = 'Flex'
