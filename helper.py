from os import path
from re import match

# obtain filepath/name to .css and .html files
def intro(hc):
    filepath, ext = '', '',
    end = -5 if hc == 'html' else -4

    count = input('Do you have more than 1 .' + hc + ' file? (yes/no): ')

    # find all files in directory
    if count.lower() in ('yes', 'y'):
        filepath = input('Path to directory (blank if PWD): ')
        ext = '*.' + hc
        if filepath != '':
            if not path.isdir(filepath):
                exit('Invalid path')

    # find 1 file
    elif count.lower() in ('no', 'n'):
        filepath = input('Path to .' + hc + ' file: ')
        if filepath[end:] != '.' + hc:
            exit('Invalid file')
        if not path.isfile(filepath):
            exit('Invalid file')
    else:
        exit('Invalid response')

    return filepath + '*.' + hc if filepath[-1:] == '/' or filepath == '' else filepath

# remove duplicates from dictionary
def remove_dups(d):
    r, l = {}, 0
    for k, v in d.items():
        if v not in r.keys():
            r[k] = v
            l += 1
    return (r, l)

# determine if line has one or multiple rules
def solo(line):
    pattern = '(\.|\#)-?[_a-zA-Z]+[_a-zA-Z0-9-]*'
    flag, end, found, count = False, False, '', 0
    for c in line:
        # found a rule
        if c == '.' or c == '#':
            flag = True
        # nevermind, start over
        if c == ';':
            flag = False
            found = ''
        # reached the end of a rule
        if c == '{' or c == ',':
            if len(found) > 0:
                if match(pattern, found):
                    count += 1
        if c == '{':
            end = True
        if flag:
            found += c
    if match(pattern, found) and not end:
        count += 1
    # single rule
    if count == 0 or count == 1:
        return True
    # multiple rules
    elif count > 1:
        return False

# removes comma if last character of string
def comma(w):
    return w[:-1] if w[-1:] == ',' else w

# look up html file in dictionary of html and css files
def lookup(d, f):
    for h, c in d.items():
        if h == f:
            return c
