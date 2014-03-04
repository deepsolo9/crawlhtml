#-*- coding: UTF-8 -*-
import urllib, urllib2, httplib, re

class Translation(object):

    url = ''

    def translateTxt(self, text):
        values = {'hl': 'zh-CN', 'ie': 'UTF-8', 'text': text.encode("utf8"), 'langpair': "'en'|'zh-CN'"}
        url = 'http://translate.google.cn/translate_t'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
        req.add_header('User-Agent', browser)
        response = urllib2.urlopen(req)
        html = response.read()
        p = re.compile('<span id=result_box[\s\S]*?</span></span>')
        m = p.search(html)
        result = re.subn('title=[\s\S]*?>', ">", m.group(0))
        text_2 = result[0].strip(';').lstrip("'").rstrip("'")
        return text_2
