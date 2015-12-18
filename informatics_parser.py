#!/usr/bin/python
# -*- coding: utf8 -*-
from time import sleep
import urllib2, cookielib

site = "http://informatics.mccme.ru/"

def parse_res(adress):
    print 'LAUNCH:',
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(site+'login/index.php')
    sleep(1)
    resp = opener.open(adress)
    the_page = resp.read()
    f = open('download.html', 'w')
    f.write(the_page)
    f.close()

    start_marker = '<td><font style="font-size:10px">Попыток</font>\n</tr>'
    start = the_page.find(start_marker)
    out = []
    the_page = the_page[start+len(start_marker):]
    print "FAILED"*int(start == -1)
    while start != -1:
        #print the_page[:100]
        start = the_page.find('<td>')
        the_page = the_page[start+4:]
        end = the_page.find('\n')
        place = the_page[0:end]
        start = the_page.find('<td>')
        the_page = the_page[start+4:]
        end = the_page.find('\n')
        name = the_page[0:end]
        start = the_page.find('<td width="25" ')
        if the_page[start+16:start+40].startswith("bgcolor"):
            the_page = the_page[start+35:]
        else:
            the_page = the_page[start+16:]
        end = the_page.find('</td>\n')
        solved = the_page[0:end]
        start = the_page.find('<td>')
        the_page = the_page[start+4:]
        end = the_page.find('</td>\n')
        penalty = the_page[0:end]
        out.append([place, name, solved, penalty])
        the_page = the_page[end+6:]
    if out:
        out = out[:-1]
        print "FINISHED"
    return out


def parse_id(id, retries=5):
    i = 0
    adress = 'http://informatics.mccme.ru/mod/statements/view3.php?chapterid='+str(id)+'&standing'
    out = []
    while not out and i < retries:
        out = parse_res(adress)
        i += 1
    print len(out), 'results read'
    return out