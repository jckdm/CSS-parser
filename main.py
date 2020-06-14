from parser import parse_css, parse_html
from cleaner import clean
from sys import exit

def main():
    c = parse_css()
    h = parse_html()
    unused = {}

    print(f'Identified {c[0][1]} unique classes and {c[1][1]} unique IDs.\n')

    for cla, num in c[0][0].items():
        if cla.split()[0] not in h[0]:
            unused[cla] = num
            print(f'Unused class:  {cla}{num}')

    for ID, num in c[1][0].items():
        if ID.split()[0] not in h[1]:
            unused[ID] = num
            print(f'Unused ID:     {ID}{num}')

    if not unused:
        print('No unused classes nor IDs!')
    else:
        q = input('\nMay I remove these unused rules and output new .css files? (yes/no): ')
        if q.lower() in ('yes', 'y'):
            clean(unused)
        elif q.lower() in ('no', 'n'):
            exit('Thank you.')
        else:
            exit('Invalid response.')

if __name__ == '__main__':
    main()
