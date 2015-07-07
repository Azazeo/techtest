__author__ = 'd.tabakerov'


from socket import timeout
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def do_request(url, name, year):
    """
    :type url: str
    :type name: str
    :type year: str
    :rtype: str
    """
    data = bytes(urlencode({'name': name, 'sex': 'M', 'start': year}), encoding='utf8')
    request = Request(url, method='POST', data=data)
    try:
        with urlopen(request, timeout=30) as r:
            d = r.read().decode('utf8')
        return d
    except URLError as e:
        print('Error on request:')
        print(e.reason)
        exit(0)
    except timeout as e:
        print('Request timeout')
        exit(0)
