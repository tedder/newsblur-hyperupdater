#!/usr/bin/python

import grequests

for x in xrange(0,100000):
  print "%i - %i" % (x*100, (x+1)*100)
  reqs = (grequests.get("http://newsblur.com/reader/feed/%i" % y) for y in xrange(x*100,(x+1)*100))
  print grequests.map(reqs)
