import parser

def main():
    c = parser.parse_css()
    h = parser.parse_html()
    flag = False

    print('Identified ' + str(len(c[0])) + ' unique classes and ' + str(len(c[1])) + ' unique IDs.\n')

    for ID, file in c[0].items():
        if ID not in h[0]:
            flag = True;
            print(f'Unused class:  {ID} : {file}')

    for ID, file in c[1].items():
        if ID not in h[1]:
            flag = True;
            print(f'Unused ID:     {ID} : {file}')

    if flag == False:
        print('No unused classes nor IDs!')

if __name__ == '__main__':
    main()
