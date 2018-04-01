#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Justin Swaney'
SITENAME = u'Justin Swaney'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Chung Lab Website', 'http://www.chunglab.org/'),
         ('Chung Lab Github', 'https://github.com/chunglabmit'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/justinmswaney?lang=en'),
          ('Facebook', 'https://www.facebook.com/jswaney2'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# For pelican-bootstrap3
THEME = 'C:/Users/Justin/pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# For the translations
PLUGIN_PATHS = ['C:/Users/Justin/pelican-plugins']
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'