# -*- coding: utf-8 -*-

AUTHOR = u'Luke and Matt Makai'
SITENAME = u'Risk Developer'
SITEURL = 'http://www.riskdeveloper.com'
TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/makaimc/riskdeveloper.com'
PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'blog', 'all')

ARTICLE_SAVE_AS = 'blog/{slug}.html'

SITEMAP_SAVE_AS = 'sitemap.xml'

FEED_DOMAIN = 'http://www.riskdeveloper.com'
FEED_RSS = 'feed'

BYLINE = '&copy; 2016 Luke and Matt Makai. All Rights Reserved.'
LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/makaimc'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

