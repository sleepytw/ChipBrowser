import re

html_example = """
<HTML>

<HEAD>

<TITLE>Your Title Here</TITLE>

</HEAD>

<BODY BGCOLOR="FFFFFF">

<CENTER><IMG SRC="clouds.jpg" ALIGN="BOTTOM"> </CENTER>

<HR>

<a href="http://somegreatsite.com">Link Name</a>

is a link to another nifty site

<H1>This is a Header</H1>

<H2>This is a Medium Header</H2>

Send me mail at <a href="mailto:support@yourcompany.com">

support@yourcompany.com</a>.

<P> This is a new paragraph!

<P> <B>This is a new paragraph!</B>

<BR> <B><I>This is a new sentence without a paragraph break, in bold italics.</I></B>

<HR>

</BODY>

</HTML>
"""

commands = [
    'html', 'head', 'body', 'title'
    ]


class HTMLParser(object):

    @classmethod
    def segregate(cls, data):
        '''
        :params rawdata: // seperating headers/&http_response from the package 
        '''

        http_response = data.find('\r\n\r\n')
        if http_response >= 0:
            return data[http_response+4:]

        return data
    
    @classmethod
    def parse(cls, rawdata, trace_all: dict = {}, trace: dict = {}) -> str:
        data  = HTMLParser.segregate(rawdata); data_cache = [] # data -> html part

        index = lambda data, command: trace.update(
                {
                    str(command): data[data.find(f'<{command}>')+len(f'<{command}>'):data.find(f'</{command}>')]
                    }

                if command in commands else None
                
            )

        for i, k in enumerate(data):
            data_cache.append(k)

        for i, k in enumerate(data_cache):
            if data_cache[i] == '>' and data_cache[i+1] != '\n':
                data_cache[i] += '\n'
            elif data_cache[i] == '<' and data_cache[i+1] == '/' and data_cache[i-2] != '\n':
                data_cache[i-1] += '\n'

        data = ''.join(data_cache)

        def index_all(data):
            for command in data.split():
                if not command.startswith('</') and command.startswith('<') and command.endswith('>'):
                    attribute = str(re.search('<(.*)>', command).group(1))
                    trace_all.update(
                        {
                            attribute.lower(): data[data.find(f'<{attribute}>')+len(f'<{attribute}>'):data.find(f'</{attribute}>')]
                        }
                    )

        index_all(data)

        print(trace_all['html'])

HTMLParser.parse(html_example)

