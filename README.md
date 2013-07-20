foaas-python
============

A simple Python library to [FOAAS].

[![Build Status](https://secure.travis-ci.org/dmpayton/foaas-python.png)](http://travis-ci.org/dmpayton/foaas-python)
[![Downloads](https://pypip.in/d/foaas/badge.png)](https://crate.io/packages/foaas/)


* **Author**: [Derek Payton]
* **Version**: 0.0.1
* **License**: [MIT]

Documentation
-------------

### Installation

This package relies on [requests] and should be installed with [pip]:

```
pip install foaas
```

### Basic Usage

Fuck off:

```
>>> from foaas import fuck
>>> print fuck.off(name='Tom', from_='Chris').text
Fuck off, Tom. - Chris
```

Give me some fucking JSON:

```
>>> fuck.that(from_='Chris').json
{u'message': u'Fuck that.', u'subtitle': u'- Chris'}
```

Just get the fucking URL:

```
>>> print fuck.everything(from_='Chris').url
http://foaas.herokuapp.com/everything/Chris
```

This needs to be fucking secure:

```
>>> from foaas import Fuck
>>> fuck = Fuck(secure=True)
>>> fucking = fuck.life(from_='Phil')
>>> print fucking.url
https://foaas.herokuapp.com/life/Phil
>>> print fucking.text
Fuck my life. - Phil
```

Give me some random fucking things:

```
>>> print fuck.random(from_='Chris').text
Fuck you very much. - Chris
>>> print fuck.random(from_='Chris').text
Fuck my life. - Chris
>>> print fuck.random(name='Tom', from_='Chris').text
Fuck me gently with a chainsaw, Tom. Do I look like Mother Teresa? - Chris
>>> print fuck.random(name='Tom', from_='Chris').text
Fuck off, Tom. - Chris
```

### Supported Actions

 * `fuck.life(from_)`
 * `fuck.everyone(from_)`
 * `fuck.that(from_)`
 * `fuck.chainsaw(name, from_)`
 * `fuck.thanks(from_)`
 * `fuck.linus(name, from_)`
 * `fuck.pink(from_)`
 * `fuck.king(name, from_)`
 * `fuck.off(name, from_)`
 * `fuck.donut(name, from_)`
 * `fuck.this(from_)`
 * `fuck.everything(from_)`
 * `fuck.shakespeare(name, from_)`
 * `fuck.you(name, from_)`
 * `fuck.random(name, from_)`

### tl;dr

```
foaas.Fuck([secure=True]).<action>(name='<name>', from_='<from>').[url|html|text|json]
```

Testing
-------

```
$ python tests.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.924s

OK
```

[FOAAS]: http://foaas.com/
[Derek Payton]: http://dmpayton.com
[MIT]: https://github.com/dmpayton/foaas-python/blob/master/LICENSE
[requests]: http://python-requests.org/
[pip]: http://www.pip-installer.org/
