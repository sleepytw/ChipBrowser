import re

from html import unescape

from html.parser import HTMLParser


def escape(s, quote=True):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (') characters are also
    translated.
    """
    s = s.replace("&", "&amp;") # Must be done first!
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    if quote:
        s = s.replace('"', "&quot;")
        s = s.replace('\'', "&#x27;")
    return s

class HTMLParser(object):

    def __init__(self, url, data, rawdata):
        self.url     = url
        self.rawdata = rawdata

    def segregate(self, xdata):
        '''
        :params rawdata: // seperating headers/&http_response from the package 
        '''
        http_response = self.xdata.find('\r\n\r\n')
        if http_response >= 0:
            return self.xdata[http_response+4:]

        return self.rawdata
    
    def parse(self):
        data = HTMLParser.segregate(self.rawdata) # data -> html part
        
