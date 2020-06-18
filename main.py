from parser import parse_css, parse_html
from cleaner import clean
from sys import exit

def main():
    c = parse_css()
    h = parse_html()
    unused, fileNames, fileCount = {}, [], 0

    for cla, num in c[0][0].items():
        x = cla.split()
        if x[0] not in h[0]:
            unused[cla] = num
            if x[2] not in fileNames:
                fileNames.append(x[2])
                fileCount += 1

    for ID, num in c[1][0].items():
        y = ID.split()
        if y[0] not in h[1]:
            unused[ID] = num
            if y[2] not in fileNames:
                fileNames.append(y[2])
                fileCount += 1

    print(f'Identified {c[0][1]} unique classes and {c[1][1]} unique IDs.\n')

    for rule, num in unused.items():
        z = rule.split()
        if ':' in z[0]:
            zz = z[0].split(':')
            if zz[0] + ' : ' + z[2] not in unused:
                continue
        if z[0][0] == '.':
            print(f'Unused class:  {rule}{num}')
        elif z[0][0] == '#':
            print(f'Unused ID:     {rule}{num}')

    if not unused:
        print('No unused classes nor IDs!')
    else:
        q = input('\nMay I remove these unused rules and output new .css files? (yes/no): ')
        if q.lower() in ('yes', 'y'):
            clean(unused, fileNames, fileCount)
        elif q.lower() in ('no', 'n'):
            exit('Thank you.')
        else:
            exit('Invalid response.')

if __name__ == '__main__':
    main()
