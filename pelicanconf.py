#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Justin Swaney'
SITENAME = u'Justin Swaney'
SITEURL = 'https://jmswaney.github.io'
RELATIVE_URLS = True # True when developing on localhost... messes up comments

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

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
		   'disqus_static',
		   'pelican_youtube',
		   'liquid_tags.include_code',]
I18N_TEMPLATES_LANG = 'en'

# Add site logo and favicon
SITELOGO = 'images/neuron_icon.png'
SITELOGO_SIZE = 30
HIDE_SITENAME = True
FAVICON = 'images/neuron_icon.png'
OPEN_GRAPH_IMAGE = 'images/hela_cells.jpg'

# Banner image - currently overridden by home.rst
BANNER = 'images/hela_cells.jpg'
BANNER_SUBTITLE = 'Scientist, Developer, Engineer'

# Sidebar
HIDE_SIDEBAR = True

# License
CC_LICENSE = "CC-BY-NC"

# AddThis sharing
ADDTHIS_PROFILE = 'ra-5ac0f7e62eb46c7e'

# Twitter card previews
TWITTER_CARDS = True
USE_OPEN_GRAPH = True

# Sometimes the Disqus server goes down and this will throw some cryptic JSONDecodeError
# Comments
DISQUS_SITENAME = u'jmswaney-github-io'
DISQUS_SECRET_KEY = u'vjASi0O1T30UrdohjeMobrjrsGXNihetP40yX9n59pHyVmpgS7t7G3KwWR5L9Osc'
DISQUS_PUBLIC_KEY = r'QGYOWjWq14FG49UwGs8TTZgp2IuSmTCEVVxTz1A5s5BySE6R29c6ZOwo5nsbW0cK'

DISQUS_NO_ID = True # Prevent possible loss of comments when switching themes
DISQUS_ID_PREFIX_SLUG = True # avoid comment clash on same slugs
# # :comments: enabled on page metadata can also allow comments on a page too
