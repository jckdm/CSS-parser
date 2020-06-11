from os import path

def intro(hc):
    filepath, ext = '', '',
    end = -5 if hc == 'html' else -4

    count = input('Do you have more than 1 .' + hc + ' file? (yes/no): ')

    if count.lower() in ('yes', 'y'):
        filepath = input('Path to directory (blank if PWD): ')
        ext = '*.' + hc
        if filepath != '':
            if not path.isdir(filepath):
                print('Invalid path')
                exit(1)

    elif count.lower() in ('no', 'n'):
        filepath = input('Path to .' + hc + ' file: ')
        if (filepath[end:] != '.' + hc):
            print('Invalid file')
            exit(2)
        if not path.isfile(filepath):
            print('Invalid file')
            exit(3)
    else:
        print('Invalid response')
        exit(4)

    if filepath[-1:] == '/' or filepath == '':
        return filepath + '*.' + hc
    else:
        return filepath

def remove_dups(d):
    r = {}
    l = 0
    for k, v in d.items():
        if v not in r.keys():
            r[k] = v
            l += 1
    return (r, l)
