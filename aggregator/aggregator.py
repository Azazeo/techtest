__author__ = 'd.tabakerov'


from functools import reduce


def calculate(data):
    """
    :type data: dict
    :rtype: float
    """
    return float(reduce(lambda x, y: x + y, data.values()))/len(data)
