import find

def main():
    c = find.parse_css()
    h = find.parse_html()

    for x in c[0]:
        if x not in h[0]:
            print("Unused class: " + x)

    for y in c[1]:
        if y not in h[1]:
            print("Unused ID: " + y)

if __name__ == "__main__":
    main()
