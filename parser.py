import find

def main():
    c = find.parse_css()
    h = find.parse_html()

    flag = False

    print()

    for x in c[0]:
        if x not in h[0]:
            flag = True;
            print('Unused class:  ' + x)

    for y in c[1]:
        if y not in h[1]:
            flag = True;
            print('Unused ID:     ' + y)

    if flag == False:
        print('No unused classes nor IDs!')

if __name__ == '__main__':
    main()
