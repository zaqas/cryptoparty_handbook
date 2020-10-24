#!/usr/bin/python

import sys, os

try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

if len(sys.argv) < 2:
    sys.exit('no parameter given')

if not os.path.exists(sys.argv[1]):
    sys.exit('file %s not found' % sys.argv[1])

h = open(sys.argv[1], 'r').read()

soup = BeautifulSoup(h)
for div in soup.html.body.findAll('div'):
    if (div.has_attr('id')) and (div['id'] == 'TOC'):
        print(div)
