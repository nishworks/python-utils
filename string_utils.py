__doc__ = """

    Useful string utilities

"""

def to_str(unicode_or_str, encoding='utf-8'):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode(encoding)
    else:
        value = unicode_or_str
    return value


def to_unicode(unicode_or_str, encoding='utf-8'):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode(encoding)
    else:
        value = unicode_or_str
    return value
