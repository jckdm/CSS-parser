from sys import exit
from glob import glob
import helper

def parse_css():
    filepath = helper.intro('css')
    classes, ids, found, flag = {}, {}, '', False

    for file in glob(filepath):
        with open(file) as f:
            print('Read ' + file)

            for line in f:
                for c in line:
                    if (c == '.') or (c == '#'):
                        flag = True
                    if (c == ';') or (c == ':'):
                        flag = False
                        found = ''
                    if (c == '{') or (c == ','):
                        if (len(found) > 0):
                            found = found.strip()
                            if (found[0] == '.'):
                                classes[found[1:]] = file
                            elif (found[0] == '#'):
                                ids[found[1:]] = file
                        flag = False
                        found = ''
                    if flag == True:
                        found += c

    if not classes and not ids:
        print('No .css files in this directory!')
        exit(5)
    else:
        return (helper.remove_dups(classes), helper.remove_dups(ids))

def parse_html():
    filepath = helper.intro('html')
    cl, id = set([]), set([])

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

    if not cl and not id:
        print('No .html files in this directory!')
        exit(6)
    else:
        return (list(cl), list(id))
