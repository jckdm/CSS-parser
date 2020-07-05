from helper import lookup
from os import path

def define(un, cf):
    up = {}
    for rule, file in un.items():
        # get name of css file
        css = lookup(cf, file)
        if not path.isfile(css):
            exit(f'Sorry, {css} is not a valid filepath.')
        # if already cleaned, open new file
        newF = css[:-4] + '-clean.css'
        css = css if not path.isfile(newF) else newF
        # count number of definitions
        if css not in up:
            up[css] = 1
        else:
            up[css] += 1
        with open(css) as og:
            data = og.read()
        # prepend new rules
        with open(css, 'w') as new:
            new.write(rule + ' {\n\t/* Define your style rule here */\n}\n' + data)
    # print changes
    for file, count in up.items():
        r = 'rules' if count > 1 else 'rule'
        print(f'Defined {count} new {r} in {file}')
