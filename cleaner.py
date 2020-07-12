from helper import solo, comma, full

def clean(u, fn, fc):
    # pre-populate arrays
    nums, rules = [[] for _ in range(fc)], [[] for _ in range(fc)]

    # extract line numbers, filenames
    for key, value in u.items():
        k, v = key.split(), value.split()[2:]
        rule, ind = k[0], fn.index(k[2])
        if rule not in rules[ind]:
            rules[ind].append(rule)
        for lineNum in v:
            n = int(comma(lineNum))
            if n not in nums[ind]:
                nums[ind].append(n)

    # for each file
    for i in range(fc):
        # sort line numbers
        nums[i].sort()
        file = fn[i]
        with open(file) as f:
            new = file[:-4] + '-clean.css'
            # open new file to write
            with open(new, 'w') as newF:
                soloFlag, multiFlag, newline, totalFlag, end = False, False, False, False, False
                # for each line
                for num, line in enumerate(f, 1):
                    # if haven't seen all problem lines
                    if nums[i]:
                        # if line has an unused rule
                        if num == nums[i][0]:
                            # remove line num about to be cleaned
                            del nums[i][0]
                            # how many rules are on this line?
                            soloFlag = solo(line)
                            multiFlag = not(soloFlag)
                            # is the entire rule defined on this line?
                            y = full(line)
                        # if multiple rules
                        if multiFlag:
                            l = line.split()
                            ll = len(l)
                            # loop thru words in rule header
                            for x in range(ll):
                                # replace unused rules with ?
                                if comma(l[x]) in rules[i]:
                                    l[x] = '?'
                            # now remove those elements, update length
                            l = [e for e in l if e != '?']
                            ll = len(l)
                            if ll > 1:
                                # adjust commas based on presence of opening brace
                                if l[ll - 1] == '{':
                                    l[ll - 2] = comma(l[ll - 2])
                                else:
                                    l[ll - 1] = comma(l[ll - 1])
                            else:
                                soloFlag = True
                                totalFlag = True
                            # re-assemble line from list
                            line = ' '.join(l) + '\n'
                            multiFlag = False
                        # if one rule
                        if soloFlag:
                            for c in line:
                                # ignore until rule closes
                                if c == '}':
                                    soloFlag = False
                                    # if all rules were removed from line
                                    if totalFlag:
                                        totalFlag = False
                        elif not soloFlag:
                            # add newlines, but never more than 1
                            if not newline or line != '\n':
                                newF.write(line)
                            newline = True if line == '\n' else False
                    # remove definition of last rule, unless it was all on one line
                    elif not nums[i] and not end and not y:
                        for c in line:
                            if end:
                                newF.write(c)
                            # keep reading until definition ends
                            if c == '}':
                                end = True
                    # no need to examine char at a time
                    else:
                        newF.write(line)

            print(f'Wrote {new}')
            newF.close()
