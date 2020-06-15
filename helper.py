from os import path
from re import match

def intro(hc):
    filepath, ext = '', '',
    end = -5 if hc == 'html' else -4

    count = input('Do you have more than 1 .' + hc + ' file? (yes/no): ')

    if count.lower() in ('yes', 'y'):
        filepath = input('Path to directory (blank if PWD): ')
        ext = '*.' + hc
        if filepath != '':
            if not path.isdir(filepath):
                exit('Invalid path')

    elif count.lower() in ('no', 'n'):
        filepath = input('Path to .' + hc + ' file: ')
        if (filepath[end:] != '.' + hc):
            exit('Invalid file')
        if not path.isfile(filepath):
            exit('Invalid file')
    else:
        exit('Invalid response')

    if filepath[-1:] == '/' or filepath == '':
        return filepath + '*.' + hc
    else:
        return filepath

def remove_dups(d):
    r = {}
    l = 0
    for k, v in d.items():
        if v not in r.keys():
            r[k] = v
            l += 1
    return (r, l)

def solo(line):
    pattern = '(\.|\#)-?[_a-zA-Z]+[_a-zA-Z0-9-]*'
    flag, found, count = False, '', 0
    for c in line:
        if (c == '.') or (c == '#'):
            flag = True
        if (c == ';') or (c == ':'):
            flag = False
            found = ''
        if (c == '{') or (c == ','):
            if len(found) > 0:
                if match(pattern, found):
                    count += 1
        if flag:
            found += c
    if count == 0 or count == 1:
        if match(pattern, found):
            count += 1
        return True
    elif count > 1:
        return False

def comma(w):
    return w[:-1] if w[-1:] == ',' else w
