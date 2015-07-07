__author__ = 'd.tabakerov'


import re


def _parsing(html):
    position_start = 0
    while position_start != -1:
        position_start = html.find('<table width=96% class=layout>')
        position_end = position_start + html[position_start:].find('</table>') + len('</table>')
        row = html[position_start:position_end]
        html = html[position_end:]
        if position_start != -1:
            row = row.replace('\n', '')
            reg = re.compile(r"(>\d+<).+(>\d)")
            res = re.search(reg, row)
            g = res.groups()
            year = int(g[0][1:len(g[0])-1])
            rate = int(g[1][1:])
            yield (year, rate)


def parse_page(page, year_end):
    year_end = int(year_end)
    return {part[0]: part[1] for part in _parsing(page) if part[0] <= year_end}