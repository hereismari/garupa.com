import re
from numbers import Integral

_required = {
    'user': {'uid', 'passwd', 'name', 'email'},
    'ride': {'date', 'dest', 'origin', 'route', 'weekly', 'seats'}
}

_pattern = {
    'uid'   : '[1-7,9][0-1][0-6][0-1][1-4][0-9]{4}',
    'passwd': '.+',
    'name'  : '.{3,}',
    'email' : '.+@.+\..+',
    'phone' : '\(\d\d\) \d{4,5}-\d{4}$',
    'photo' : 'data:image/.+;base64,[A-Za-z0-9+/]*={0,2}$',

    'date'  : '\d{13}$',
    'dest'  : '(HOME|UFCG)$',
    'origin': '.{12,}',
    'route' : "\[u'[^']{5,}'(, u'[^']{5,}')*]$",
    'weekly': '(True|False)$',
    'seats' : '\d{1,2}$'
}

_type = {
    'uid'   : Integral,
    'passwd': object,
    'name'  : unicode,
    'email' : unicode,
    'phone' : unicode,
    'photo' : unicode,

    'date'  : Integral,
    'dest'  : unicode,
    'origin': unicode,
    'route' : list,
    'weekly': bool,
    'seats' : Integral
}

def check(attr, value):
    typed = isinstance(value, _type[attr])
    formated = re.match(_pattern[attr], unicode(value))
    return typed and formated

def complete(mode, obj):
    return set(obj) == _required[mode]
