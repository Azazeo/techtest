#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3
__author__ = 'd.tabakerov'


from sys import argv

from aggregator import calculate
from connector import do_request
from parser import parse_page


if __name__ == '__main__':
    if len(argv) < 4:
        print('Not enough args\nProvide name, start year and end year')
        exit(0)
    name = argv[1]
    year_start = argv[2]
    year_end = argv[3]
    try:
        _ = int(year_start)
        _ = int(year_end)
    except ValueError as e:
        print('Error in entered date')
        exit(0)
    if int(year_end) < int(year_start):
        print('End year cannot be before start year')
        exit(0)
    if int(year_start) < 1880:
        print('Warning: no data before 1880, start year will be set to 1880')
        year_start = '1880'

    page = do_request('http://www.socialsecurity.gov/cgi-bin/babyname.cgi', name, year_start)
    data = parse_page(page, year_end)
    if len(data) > 0:
        result = calculate(data)
        print("Between {} and {} the average popularity rank of the name {} was {:.2f}".
              format(year_start, year_end, name, result))
    else:
        print("No data found for name '{}'".format(name))
