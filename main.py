import parser

def main():
    c = parser.parse_css()
    h = parser.parse_html()
    flag = False

    print('\nIdentified ' + str(len(c[0])) + ' unique classes and ' + str(len(c[1])) + ' unique IDs.\n')

    for key, value in c[0].items():
        if key not in h[0]:
            flag = True;
            print(f'Unused class:  {key} : {value}')

    for y in c[1]:
        if y not in h[1]:
            flag = True;
            print('Unused ID:     ' + y)

    if flag == False:
        print('No unused classes nor IDs!')

if __name__ == '__main__':
    main()
