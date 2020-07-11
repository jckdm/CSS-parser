from sys import exit
from glob import glob
from helper import intro, remove_dups
from re import match

def parse_css():
    # obtain filename/path
    filepath = intro('css')
    classes, ids, found, flag = {}, {}, '', False

    # read each file
    for file in glob(filepath):
        with open(file) as f:
            for num, line in enumerate(f, 1):
                for c in line:
                    # found a rule
                    if c == '.' or c == '#':
                        flag = True
                    # nevermind
                    if c == ';':
                        flag, found = False, ''
                    # rule is ending
                    if c == '{' or c == ',':
                        if len(found) > 0:
                            found = found.strip()
                            # check for invalid chars
                            if match('(\.|\#)-?[_a-zA-Z]+[_a-zA-Z0-9-]*', found):
                                found += ' : ' + file
                                # if brace on own line, rule is on line before
                                if line == '{\n':
                                    num -= 1
                                sNum = str(num)
                                # found a class
                                if found[0] == '.':
                                    if found in classes:
                                        # avoid multiple occurrences on same line
                                        if sNum not in classes[found]:
                                            classes[found] += ', ' + sNum
                                    else:
                                        classes[found] = ', line ' + sNum
                                # found an ID
                                elif found[0] == '#':
                                    if found in ids:
                                        if sNum not in ids[found]:
                                            ids[found] += ', ' + sNum
                                    else:
                                        ids[found] = ', line ' + sNum
                            flag = False
                            found = ''
                    if flag:
                        found += c
        print(f'Read {file}')

    if not classes and not ids:
        exit('No .css files in this directory!')
    else:
        return (remove_dups(classes), remove_dups(ids))

def parse_html():
    # obtain filename/path
    filepath = intro('html')
    cl, id, css, fc = [], [], {}, 0

    # read each file
    for file in glob(filepath):
        with open(file) as f:
            # append a dict for each file
            cl.append({})
            id.append({})

            for num, line in enumerate(f, 1):
                # split line into words
                words = line.split()
                for piece in words:
                    found, start = '', None
                    # found an ID
                    if piece[:2] == 'id':
                        start, found = 4, '#'
                    # found a class
                    elif piece[:5] == 'class':
                        start, found = 7, '.'
                    # found a link
                    elif piece[:4] == 'href':
                        start = 6
                    if start:
                        for char in piece[start:]:
                            if char != "'" and char != '"':
                                found += char
                            # at end, marked by quotes
                            else:
                                if start == 4:
                                    id[fc][found] = file
                                elif start == 7:
                                    cl[fc][found] = file
                                # if link to .css file
                                elif start == 6 and found[-4:] == '.css':
                                    if file not in css:
                                        css[file] = found
                                break
        print(f'Read {file}')
        fc += 1

    if not cl and not id:
        exit('No .html files in this directory!')
    else:
        return ((cl, id), css)
