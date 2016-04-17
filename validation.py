import re

EDITABLE = {'name', 'email', 'phone', 'photo'}
REQUIRED = {'name', 'uid', 'email', 'passwd'}

_pattern = {
    'name'  : '.{3,}',
    'uid'   : '\d{9}$',
    'email' : '.+@.+\..+',
    'passwd': '.+',
    'phone' : '\(\d\d\) \d{4,5}-\d{4}$',
    'photo' : 'data:image/.+;base64,[A-Za-z0-9+/]*={0,2}$'
}

def check(attr, value):
    return re.match(_pattern[attr], value)