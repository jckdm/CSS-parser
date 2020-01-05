import sys
import os
import glob
import re
from bs4 import BeautifulSoup

def parse_css():
    filename = input("Name of CSS file: ")

    if (filename[len(filename)-4:] != ".css"):
        print("Invalid file extension")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("Invalid file")
        sys.exit(2)

    with open(filename) as f:
        classes = set([])
        ids = set([])
        while True:
            c = f.read(1)

            if (c == ".") or (c == "#"):
                found = "" + c
                cc = ""
                while (cc != "{") and (cc != ","):
                    cc = f.read(1)
                    if (cc == ";") or (cc == ":"):
                        found = ""
                        break
                    elif (cc != "{") and (cc != ","):
                        found += cc
                if (len(found) > 0):
                    found = found.strip()
                    if (found[0] == "."):
                        classes.add(found[1:])
                    elif (found[0] == "#"):
                        ids.add(found[1:])
            if not c:
                return (classes, ids)
                break


def parse_html():
    c = set([])
    i = set([])
    for filename in glob.glob('*.html'):
        with open(filename) as f:
            soup = BeautifulSoup(f, "html.parser")
            classes = [value for element in soup.find_all(class_=True) for value in element["class"]]

            tags = set([])

            for tag in soup.find_all(re.compile("^")):
                tags.add(tag.name)

            for tag in tags:
                for line in soup.find_all(tag):
                    id = line.get('id')
                    if id is not None:
                        i.add(id)

        for item in classes:
            c.add(item)

    return (list(c), list(i))
