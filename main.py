from parser import parse_css, parse_html
from cleaner import clean
from sys import exit

def main():
    c = parse_css()
    h = parse_html()
    unused, fileNames, css, fileCount = {}, [], [], 0

    for cla, num in c[0][0].items():
        x = cla.split()
        if ':' not in x[0]:
            css.append(x[0])
        if x[0] not in h[0][0]:
            unused[cla] = num

    for ID, num in c[1][0].items():
        y = ID.split()
        if ':' not in y[0]:
            css.append(y[0])
        if y[0] not in h[1][0]:
            unused[ID] = num

    print(f'\nIdentified {c[0][1]} unique classes and {c[1][1]} unique IDs.\n')

    for d in h:
        for dd in d:
            for rule, num in dd.items():
                if rule not in css:
                    pre = 'ID:   ' if rule[0] == '#' else 'class:'
                    print(f'Undefined {pre} {rule} : {num}')
    print()

    final = dict(unused)

    for rule, num in unused.items():
        z = rule.split()
        if z[2] not in fileNames:
            fileNames.append(z[2])
            fileCount += 1
        if ':' in z[0]:
            zz = z[0].split(':')
            if zz[0] + ' : ' + z[2] not in unused:
                del final[rule]
                continue
        if z[0][0] == '.':
            print(f'Unused class:    {rule}{num}')
        elif z[0][0] == '#':
            print(f'Unused ID:       {rule}{num}')

    if not final:
        print('No unused classes nor IDs!')
    else:
        q = input('\nMay I remove these unused rules and output new .css files? (yes/no): ')
        if q.lower() in ('yes', 'y'):
            clean(final, fileNames, fileCount)
        elif q.lower() in ('no', 'n'):
            exit('Thank you.')
        else:
            exit('Invalid response.')

if __name__ == '__main__':
    main()
