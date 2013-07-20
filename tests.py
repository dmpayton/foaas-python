import unittest
from foaas import Fuck


class FOAASTests(unittest.TestCase):
    def setUp(self):
        self.fuck = Fuck()

    def test_url(self):
        url = self.fuck.off(name='Alice', from_='Bob').url
        self.assertEqual('http://foaas.herokuapp.com/off/Alice/Bob', url)

    def test_url_secure(self):
        secure_fuck = Fuck(secure=True)
        url = secure_fuck.everything(from_='Bob', secure=True).url
        self.assertEqual('https://foaas.herokuapp.com/everything/Bob', url)

    def test_url_quoting(self):
        url = self.fuck.donut(name='Alice!', from_='Bobby McGee').url
        self.assertEqual('http://foaas.herokuapp.com/donut/Alice%21/Bobby%20McGee', url)

    def test_html(self):
        html = self.fuck.thanks(from_='Bob').html
        self.assertIn('<h1>Fuck you very much.</h1>', html)
        self.assertIn('<em>- Bob</em>', html)

    def test_json(self):
        json = self.fuck.life(from_='Bob').json
        self.assertEqual({
            'message': 'Fuck my life.',
            'subtitle': '- Bob'
        }, json)

    def test_text(self):
        text = self.fuck.thanks(from_='Bob').text
        self.assertEqual('Fuck you very much. - - Bob', text)

    def test_random(self):
        self.fuck.random(from_='Chris')
        self.fuck.random(name='Tom', from_='Chris')


if __name__ == '__main__':
    unittest.main()
