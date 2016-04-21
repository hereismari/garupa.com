import re
from distutils.util import strtobool

_required = {
    'user': {'uid', 'passwd', 'name', 'email'},
    'ride': {'date', 'dest', 'origin', 'route', 'weekly', 'seats'}
}

_pattern = {
    'uid'   : '\d{9}$',
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
    'uid'   : int,
    'passwd': unicode,
    'name'  : unicode,
    'email' : unicode,
    'phone' : unicode,
    'photo' : unicode,

    'date'  : long,
    'dest'  : unicode,
    'origin': unicode,
    'route' : list,
    'weekly': bool,
    'seats' : int
}

def check(attr, value):
    typed = type(value) is _type[attr]
    formated = re.match(_pattern[attr], unicode(value))
    return typed and formated

def complete(mode, obj):
    return set(obj) == _required[mode]
