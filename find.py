import sys
import os

filename = input("Name of CSS file: ")
if not os.path.isfile(filename):
    print("Invalid file")
    sys.exit()

with open(filename) as f:
    classes = []
    ids = []
    while True:
        c = f.read(1)

        if (c == ".") or (c == "#"):
            found = "" + c
            cc = ""
            while (cc != "{"):
                cc = f.read(1)
                if (cc == ";") or (cc == ":"):
                    found = ""
                    break
                elif (cc != "{"):
                    found += cc
            if (len(found) > 0):
                found = found.strip()
                if (found[0] == "."):
                    classes.append(found)
                elif (found[0] == "#"):
                    ids.append(found)
        if not c:
            print(classes, ids)
            break
