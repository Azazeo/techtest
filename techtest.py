__author__ = 'd.tabakerov'


from sys import argv

from aggregator import calculate
from connector import do_request
from parser import parse_page


if __name__ == '__main__':
    name = argv[1]
    year_start = argv[2]
    year_end = argv[3]
    page = do_request('http://www.socialsecurity.gov/cgi-bin/babyname.cgi', name, year_start)
    data = parse_page(page, year_end)
    result = calculate(data)
    print("Between {} and {} the average popularity rank of the name {} was {:.2f}".
          format(year_start, year_end, name, result))