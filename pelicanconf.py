#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Justin Swaney'
SITENAME = u'Justin Swaney'
SITEURL = 'http://jmswaney.github.io'
# RELATIVE_URLS = True # Only True when developing on localhost

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Manually add menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Research', '/category/research.html'),
    ('Publications', '/pages/publications.html'),
    ('About', '/pages/about.html'),
    ('Contact', '/pages/contact.html'),
)

# Blogroll
LINKS = (('Chung Lab Website', 'http://www.chunglab.org/'),
         ('Chung Lab Github', 'https://github.com/chunglabmit'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/justinmswaney?lang=en', 'twitter'),
          ('Facebook', 'https://www.facebook.com/jswaney2', 'facebook-f'),)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# For pelican-bootstrap3
THEME = 'pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_FLUID = False # Not sure what the container-fluid is

# Load plugins
PLUGIN_PATHS = ['C:/Users/Justin/pelican-plugins']
PLUGINS = ['i18n_subsites',
		   'related_posts',
		   'disqus_static',]
I18N_TEMPLATES_LANG = 'en'

# Add site logo and favicon
SITELOGO = 'images/neuron_icon.png'
SITELOGO_SIZE = 30
HIDE_SITENAME = True
FAVICON = 'images/neuron_icon.png'

# Banner image - currently overridden by home.rst
BANNER = 'images/hela_cells.jpg'
BANNER_SUBTITLE = 'Scientist, Developer, Engineer (in no particular order)'

# Sidebar
HIDE_SIDEBAR = True

# License
CC_LICENSE = "CC-BY-NC"

# AddThis sharing
ADDTHIS_PROFILE = 'ra-5ac0f7e62eb46c7e'

# Twitter card previews
TWITTER_CARDS = True

# Comments
DISQUS_SITENAME = u'jmswaney-github-io'
DISQUS_SECRET_KEY = u'vjASi0O1T30UrdohjeMobrjrsGXNihetP40yX9n59pHyVmpgS7t7G3KwWR5L9Osc'
DISQUS_PUBLIC_KEY = u'QGYOWjWq14FG49UwGs8TTZgp2IuSmTCEVVxTz1A5s5BySE6R29c6ZOwo5nsbW0cK'

DISQUS_NO_ID = True # Prevent possible loss of comments when switching themes
DISQUS_ID_PREFIX_SLUG = True # avoid comment clash on same slugs
# :comments: enabled on page metadata can also allow comments on a page too
