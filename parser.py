from sys import exit
from glob import glob
from helper import intro, remove_dups
from re import match

def parse_css():
    filepath = intro('css')
    classes, ids, found, flag = {}, {}, '', False

    for file in glob(filepath):
        with open(file) as f:
            print(f'Read {file}')

            for num, line in enumerate(f, 1):
                for c in line:
                    if c == '.' or c == '#':
                        flag = True
                    if c == ';':
                        flag = False
                        found = ''
                    if c == '{' or c == ',':
                        if len(found) > 0:
                            found = found.strip()
                            if match('(\.|\#)-?[_a-zA-Z]+[_a-zA-Z0-9-]*', found):
                                found += ' : ' + file
                                if line == '{\n':
                                    num -= 1
                                sNum = str(num)
                                if found[0] == '.':
                                    if found in classes:
                                        if sNum not in classes[found]:
                                            classes[found] += ', ' + sNum
                                    else:
                                        classes[found] = ', line ' + sNum
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

    if not classes and not ids:
        exit('No .css files in this directory!')
    else:
        return (remove_dups(classes), remove_dups(ids))

def parse_html():
    filepath = intro('html')
    cl, id, fc = [], [], 0

    for file in glob(filepath):
        with open(file) as f:
            print(f'Read {file}')
            cl.append({})
            id.append({})

            for num, line in enumerate(f, 1):
                words = line.split()
                for piece in words:
                    found, start = '', None
                    if piece[:2] == 'id':
                        start, found = 4, '#'
                    elif piece[:5] == 'class':
                        start, found = 7, '.'
                    if start != None:
                        for char in piece[start:]:
                            if char != "'" and char != '"':
                                found += char
                            else:
                                if start == 4:
                                    id[fc][found] = file
                                elif start == 7:
                                    cl[fc][found] = file
                                break
        fc += 1

    if not cl and not id:
        exit('No .html files in this directory!')
    else:
        return (cl, id)
