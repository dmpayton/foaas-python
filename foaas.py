import random
import requests
from optparse import OptionParser

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

__AUTHOR__ = 'Derek Payton <derek.payton@gmail.com>'
__LICENSE__ = 'MIT'
__VERSION__ = '0.2.0'


class FuckingResponse(object):
    ''' Takes care of making the actual request in the specified format. '''
    def __init__(self, url, language=None):
        self.url = url
        self.language = language
        self.is_secure = url.startswith('https')
        self._html = None
        self._json = None
        self._text = None

    def make_request(self, accept):
        return requests.get(self.url, headers={
            'Accept': accept,
            'Accept-Language': self.language or 'en-us'
        })

    @property
    def text(self):
        if self._text is None:
            self._text = self.make_request('text/plain')
        return self._text.text

    @property
    def json(self):
        if self._json is None:
            self._json = self.make_request('application/json')
        return self._json.json()

    @property
    def html(self):
        if self._html is None:
            self._html = self.make_request('text/html')
        return self._html.text


class Fuck(object):
    actions = {
        'awesome': 'awesome/{from}',
        'ballmer': 'ballmer/{name}/{company}/{from}',
        'because': 'because/{from}',
        'bus': 'bus/{name}/{from}',
        'bye': 'bye/{from}',
        'caniuse': 'caniuse/{name}/{from}',
        'chainsaw': 'chainsaw/{name}/{from}',
        'cool': 'cool/{from}',
        'diabetes': 'diabetes/{from}',
        'donut': 'donut/{name}/{from}',
        'everyone': 'everyone/{from}',
        'everything': 'everything/{from}',
        'fascinating': 'fascinating/{from}',
        'field': 'field/{name}/{from}/{reference}',
        'flying': 'flying/{from}',
        'king': 'king/{name}/{from}',
        'life': 'life/{from}',
        'linus': 'linus/{name}/{from}',
        'madison': 'madison/{name}/{from}',
        'nugget': 'nugget/{name}/{from}',
        'off': 'off/{name}/{from}',
        'outside': 'outside/{name}/{from}',
        'pink': 'pink/{from}',
        'thanks': 'thanks/{from}',
        'that': 'that/{from}',
        'thing': '{thing}/{from}',
        'this': 'this/{from}',
        'shakespeare': 'shakespeare/{name}/{from}',
        'what': 'what/{from}',
        'xmas': 'xmas/{name}/{from}',
        'yoda': 'yoda/{name}/{from}',
        'you': 'you/{name}/{from}',
    }

    def __init__(self, secure=False, language=None):
        self.secure = secure
        self.language = language

    def __getattr__(self, attr):
        path = self.actions.get(attr)
        if path is None:
            raise AttributeError

        def outer(path):
            def inner(secure=False, **kwargs):
                url = self.build_url(path, **kwargs)
                return FuckingResponse(url, language=self.language)
            return inner

        return outer(self.actions[attr])

    def random(self, **kwargs):
        applicable_actions = []
        for action in self.actions.keys():
            uri = self.actions[action]
            if uri.count('{') != len(kwargs):
                continue
            for param in kwargs:
                if '{{{0}}}'.format(param.rstrip('_')) not in uri:
                    break
            else:
                applicable_actions.append(action)

        choice = getattr(self, random.choice(applicable_actions))
        return choice(**kwargs)

    def build_url(self, path, **kwargs):
        # use from_ since from is a keyword. *grumble*
        params = dict([(k.rstrip('_'), quote(v)) for k, v
            in kwargs.items() if v])
        url = '{protocol}://foaas.herokuapp.com/{path}'.format(
            protocol='https' if self.secure else 'http',
            path=path.format(**params))
        return url


fuck = Fuck()

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-a', '--action', dest='action', default='off',
        help='Name of the action to perform')

    parser.add_option('-n', '--name', dest='name',
        help='Who do you want to fuck off?')

    parser.add_option('-f', '--from', dest='from', help='Who are you?')

    parser.add_option('-c', '--company', dest='company',
        help='Which company do you want to fuck off?')

    parser.add_option('-t', '--thing', dest='thing',
        help='What thing do you want to fuck off?')

    parser.add_option('-r', '--reference', dest='reference',
        help='Who do you want to reference?')

    parser.add_option('-u', '--url', action='store_true', dest='url',
        help='Only display the URL (useful for c/ping)')

    (options, args) = parser.parse_args()

    options = vars(options)
    action = options.pop('action')
    url_only = options.pop('url')

    fucking = getattr(fuck, action)(**options)
    if url_only:
        print(fucking.url)
    else:
        print(fucking.text)
