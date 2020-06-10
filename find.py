from sys import exit
from os import path
from glob import glob

def intro(hc):
    filepath, ext = '', '',
    type = 'html' if hc == True else 'css'
    end = -5 if hc == True else -4

    count = input('Do you have more than 1 .' + type + ' file? (yes/no): ')

    if count.lower() in ('yes', 'y'):
        filepath = input('Path to directory (blank if PWD): ')
        ext = '*.' + type

        if filepath != '':
            if not path.isdir(filepath):
                print('Invalid path')
                exit(1)

    elif count.lower() in ('no', 'n'):
        filepath = input('Path to .' + type + ' file: ')

        if (filepath[end:] != '.' + type):
            print('Invalid file')
            exit(2)

        if not path.isfile(filepath):
            print('Invalid file')
            exit(3)
    else:
        print('Invalid response')
        exit(4)

    if filepath[-1:] == '/' or filepath == '':
        return filepath + '*.' + type
    else:
        return filepath

def parse_css():
    filepath = intro(False)
    classes = set([])
    ids = set([])

    for file in glob(filepath):
        with open(file) as f:
            print('Read ' + file)
            while True:
                c = f.read(1)
                if (c == '.') or (c == '#'):
                    cc, found = '', '' + c
                    while (cc != '{') and (cc != ','):
                        cc = f.read(1)
                        if (cc == ';') or (cc == ':'):
                            found = ''
                            break
                        elif (cc != '{') and (cc != ','):
                            found += cc
                    if (len(found) > 0):
                        found = found.strip()
                        if (found[0] == '.'):
                            classes.add(found[1:])
                        elif (found[0] == '#'):
                            ids.add(found[1:])
                if not c:
                    break

    if not classes or not ids:
        print('No .css files in this directory!')
        exit(5)
    else:
        return (classes, ids)

def parse_html():
    filepath = intro(True)
    cl = set([])
    id = set([])

    for filename in glob(filepath):
        with open(filename) as f:
            print('Read ' + filename)

            for line in f:
                words = line.split()
                for piece in words:
                    found, start = '', None
                    if piece[:2] == 'id':
                        start = 4
                    elif piece[:5] == 'class':
                        start = 7

                    if start != None:
                        for char in piece[start:]:
                            if (char != "'") and (char != '"'):
                                found += char
                            else:
                                if start == 4:
                                    id.add(found)
                                elif start == 7:
                                    cl.add(found)

    if not cl or not id:
        print('No .html files in this directory!')
        exit(6)
    else:
        return (list(cl), list(id))
