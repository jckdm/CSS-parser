import parser

def main():
    c = parser.parse_css()
    h = parser.parse_html()

    flag = False

    print(f'Identified {c[0][1]} unique classes and {c[1][1]} unique IDs.\n')

    for cla, file in c[0][0].items():
        if cla not in h[0]:
            flag = True;
            print(f'Unused class:  {cla} : {file}')

    for ID, file in c[1][0].items():
        if ID not in h[1]:
            flag = True;
            print(f'Unused ID:     {ID} : {file}')

    if flag == False:
        print('No unused classes nor IDs!')

if __name__ == '__main__':
    main()
