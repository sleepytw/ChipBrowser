import re

html_example = """
<html>
<head>
  <title>A Meaningful Page Title<title/>
<head/>
<body>

The content of the document......

<body/>
<html/>
"""

commands = [
    'html', 'head', 'body', 'title'
    ]


class HTMLParser(object):

    @classmethod
    def segregate(cls, xdata):
        '''
        :params rawdata: // seperating headers/&http_response from the package 
        '''

        http_response = xdata.find('\r\n\r\n')
        if http_response >= 0:
            return xdata[http_response+4:]

        return xdata
    
    @classmethod
    def parse(cls, rawdata, trace: dict = {}) -> str:
        data = HTMLParser.segregate(rawdata) # data -> html part

        def index(command): 
            try:
                return trace.update(
                    {
                        str(command): data[data.find(f'<{command}>')+len(f'<{command}>'):data.find(f'<{command}/>')]
                        }
                    )
            except:
                print('An error occurred while parsing the data.')
        

