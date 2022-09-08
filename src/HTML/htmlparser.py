import re

class HTMLParser(object):

    commands = [
    'html', 'head', 'body', 'title'
    ]

    trace     : dict = {}
    trace_all : dict = {}

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
    def parse(cls, rawdata, preset: bool) -> str:
        data  = HTMLParser.segregate(rawdata); data_cache = [] # data -> html part

        index = lambda data, command: HTMLParser.trace.update(
                {
                    str(command): data[data.find(f'<{command}>')+len(f'<{command}>'):data.find(f'</{command}>')]
                    }

                if command in HTMLParser.commands else None
                
            )

        for i, k in enumerate(data):
            data_cache.append(k)

        for i, k in enumerate(data_cache):
            if data_cache[i] == '>' and data_cache[i+1] != '\n':
                data_cache[i] += '\n'
            elif data_cache[i] == '<' and data_cache[i+1] == '/' and data_cache[i-2] != '\n':
                data_cache[i-1] += '\n'


        def index_all(data):
            data = ''.join(data_cache)

            for command in data.split():
                if not command.startswith('</') and command.startswith('<') and command.endswith('>'):
                    attribute = str(re.search('<(.*)>', command).group(1))
                    HTMLParser.trace_all.update(
                        {
                            attribute.lower(): data[data.find(f'<{attribute}>')+len(f'<{attribute}>'):data.find(f'</{attribute}>')]
                        }
                    )

        if preset is True:
            for set in data:
                index(set)

        index_all(data)

