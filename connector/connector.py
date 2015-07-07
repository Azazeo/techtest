__author__ = 'd.tabakerov'


from urllib.request import Request, urlopen
from urllib.parse import urlencode


def do_request(url, name, year):
    """
    :type url: str
    :type name: str
    :type year: str
    :rtype: str
    """
    data = bytes(urlencode({'name': name, 'sex': 'M', 'start': year}), encoding='utf8')
    request = Request(url, method='POST', data=data)
    with urlopen(request) as r:
        d = r.read().decode('utf8')
    return d

