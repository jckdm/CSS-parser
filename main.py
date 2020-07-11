from parser import parse_css, parse_html
from cleaner import clean
from definer import define
from sys import exit

def main():
    # parse the files
    c = parse_css()
    h = parse_html()
    unused, undefined, results, fileNames, css, fileCount = {}, {}, '', [], [], 0

    # identify UNUSED classes
    for cla, num in c[0][0].items():
        x = cla.split()
        # no psuedoclasses allowed
        if ':' not in x[0]:
            css.append(x[0])
        if x[0] not in h[0][0][0]:
            unused[cla] = num

    # identify UNUSED IDs
    for ID, num in c[1][0].items():
        y = ID.split()
        # no psuedoclasses allowed
        if ':' not in y[0]:
            css.append(y[0])
        if y[0] not in h[0][1][0]:
            unused[ID] = num

    i = f'Identified {c[0][1]} unique classes and {c[1][1]} unique IDs.\n'
    print('\n' + i)
    results += i

    # identify UNDEFINED classes and IDs
    for d in h[0]:
        for dd in d:
            for rule, file in dd.items():
                if rule not in css:
                    undefined[rule] = file
                    pre = 'ID:   ' if rule[0] == '#' else 'class:'
                    o = f'Undefined {pre} {rule} : {file}'
                    print(o)
                    results += '\n' + o
    print()
    results += '\n'

    # copy to allow deleting
    final = dict(unused)

    # identify pseudoclasses
    for rule, num in unused.items():
        z = rule.split()
        r, fn = z[0], z[2]
        # get filenames
        if fn not in fileNames:
            fileNames.append(fn)
            fileCount += 1
        # if pseudoclass
        if ':' in r:
            rr = r.split(':')[0]
            # if rule exists and isn't unused
            if rr in css and rr + ' : ' + fn not in unused:
                del final[rule]
                continue
        o = ''
        if z[0][0] == '.':
            o = f'Unused class:    {rule}{num}'
        elif z[0][0] == '#':
            o = f'Unused ID:       {rule}{num}'
        print(o)
        results += '\n' + o

    # predefined in case file is already clean
    q, qq = 'no', 'no'
    if not final:
        o = 'No unused classes nor IDs!'
        print(o)
        results += i
    if final:
        q = input('\nMay I remove these unused rules and output new .css files? (yes/no): ')
        if q.lower() in ('yes', 'y'):
            clean(final, fileNames, fileCount)
    if not undefined:
        o = 'No undefined classes nor IDs!'
        print(o)
        results += i
    if undefined:
        qq = input('May I add definitions for undefined rules? (yes/no): ')
        if qq.lower() in ('yes', 'y'):
            define(undefined, h[1])

    if q.lower() in ('no', 'n') and qq.lower() in ('no', 'n'):
        qqq = input('Would you instead like a .txt file with your results? (yes/no): ')
        if qqq.lower() in ('yes', 'y'):
            with open('results.txt', 'w') as f:
                f.write(results)
                print('Wrote results.txt')
        elif qqq.lower() in ('no', 'n'):
            exit('Thank you.')
        else:
            exit('Invalid response.')
    else:
        exit('Thank you.')

if __name__ == '__main__':
    main()
