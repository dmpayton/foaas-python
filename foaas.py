import random
import requests
import urllib
from optparse import OptionParser

__AUTHOR__ = 'Derek Payton <derek.payton@gmail.com>'
__LICENSE__ = 'MIT'
__VERSION__ = '0.0.1'


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
        'off': 'off/{name}/{from}',
        'you': 'you/{name}/{from}',
        'this': 'this/{from}',
        'that': 'that/{from}',
        'everything': 'everything/{from}',
        'everyone': 'everyone/{from}',
        'donut': 'donut/{name}/{from}',
        'shakespeare': 'shakespeare/{name}/{from}',
        'linus': 'linus/{name}/{from}',
        'king': 'king/{name}/{from}',
        'pink': 'pink/{from}',
        'life': 'life/{from}',
        'chainsaw': 'chainsaw/{name}/{from}',
        'thanks': 'thanks/{from}',
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
        actions = self.actions.keys()
        if 'name' not in kwargs:
            actions = [key for key in actions if '{name}' not in self.actions[key]]
        return getattr(self, random.choice(actions))(**kwargs)

    def build_url(self, path, **kwargs):
        # use from_ since from is a keyword. *grumble*
        params = dict([(k.rstrip('_'), urllib.quote(v)) for k, v in kwargs.items() if v])
        url = '{protocol}://foaas.herokuapp.com/{path}'.format(
            protocol='https' if self.secure else 'http',
            path=path.format(**params))
        return url


fuck = Fuck()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-a', '--action', dest='action', help='Name of the action to perform', default='off')
    parser.add_option('-n', '--name', dest='name', help='Who do you want to fuck off?')
    parser.add_option('-f', '--from', dest='from', help='Who are you?')
    parser.add_option('-u', '--url', action='store_true', dest='url', help='Only display the URL (useful for c/ping)')

    (options, args) = parser.parse_args()

    options = vars(options)
    action = options.pop('action')
    url_only = options.pop('url')

    fucking = getattr(fuck, action)(**options)
    if url_only:
        print fucking.url
    else:
        print fucking.text
