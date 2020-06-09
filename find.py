from sys import exit
from os import path
from glob import glob

def parse_css():
    filename = input('Path to CSS file: ')

    if (filename[len(filename)-4:] != '.css'):
        print('Invalid file extension')
        exit(1)

    if not path.isfile(filename):
        print('Invalid file')
        exit(2)

    with open(filename) as f:
        classes = set([])
        ids = set([])
        while True:
            c = f.read(1)

            if (c == '.') or (c == '#'):
                found = '' + c
                cc = ''
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
                return (classes, ids)


def parse_html():
    cl = set([])
    id = set([])

    flag = False

    for filename in glob('*.html'):
        with open(filename) as f:
            flag = True
            while True:
                c = f.read(1)
                if (c == 'i'):
                    last = f.tell()
                    next = f.read(3)
                    if (next == 'd="') or (next == "d='"):
                        found = ''
                        cc = ''
                        while (cc != '"') and (cc != "'"):
                            cc = f.read(1)
                            found += cc
                        if (len(found) > 0):
                            id.add(found[:-1])
                    else:
                        f.seek(last)
                elif (c == 'c'):
                    last = f.tell()
                    next = f.read(6)
                    if (next == 'lass="') or (next == "lass='"):
                        found = ''
                        cc = ''
                        while (cc != '"') and (cc != "'"):
                            cc = f.read(1)
                            found += cc
                        if (len(found) > 0):
                            cl.add(found[:-1])
                    else:
                        f.seek(last)
                if not c:
                    return (list(cl), list(id))

    if flag == False:
        print('No .html files in this directory!')
        exit(3)
