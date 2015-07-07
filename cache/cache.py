__author__ = 'd.tabakerov'


def get_val_from_cache(name, year_start, year_end):
    try:
        f = open('.cache')
        for line in f:
            if line.split('\t')[0] == name+year_start+year_end:
                return line.split('\t')[1].replace('\n', '')
        return None
    except FileNotFoundError as e:
        return None


def write_val_to_cache(name, year_start, year_end, val):
    f = open('.cache', 'a')
    f.write(name+year_start+year_end+'\t'+val+'\n')