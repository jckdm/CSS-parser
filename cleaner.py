from helper import solo, comma

def clean(u, fn, fc):
    # pre-populate arrays
    nums, rules, numItems = [[]] * fc, [[]] * fc, [0] * fc

    # extract line numbers, filenames
    for key, value in u.items():
        k, v = key.split(), value.split()[2:]
        rule = k[0]
        ind = fn.index(k[2])
        # for each line number
        for i in range(len(v)):
            # append line numbers
            nums[ind].append(int(comma(v[i])))
            if rule not in rules[ind]:
                # and rules to remove, by file
                rules[ind].append(rule)
            numItems[ind] += 1

    # for each file
    for i in range(fc):
        # sort by line number
        nums[i].sort()
        index, file = 0, fn[i]
        with open(file) as f:
            new = file[:-4] + '-clean.css'
            print(f'Wrote {new}')

            # open new file to write
            with open(new, 'w') as newF:
                soloFlag, multiFlag, newline, totalFlag = False, False, False, False
                for num, line in enumerate(f, 1):
                    # if haven't yet removed all items
                    if index < numItems[i]:
                        # if line has an unused rule
                        if num == nums[i][index]:
                            x = solo(line)
                            soloFlag = x
                            multiFlag = not(x)
                        # if multiple rules
                        if multiFlag:
                            l = line.split()
                            ll = len(l)
                            for x in range(ll):
                                # replace unused rules with ?
                                if comma(l[x]) in rules[i]:
                                    l[x] = '?'
                                    index += 1
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
                            line = ' '.join(l) + '\n'
                            multiFlag = False
                        # if one rule
                        if soloFlag:
                            for c in line:
                                # ignore until rule closes
                                if c == '}':
                                    soloFlag = False
                                    if totalFlag:
                                        totalFlag = False
                                    else:
                                        index += 1
                        elif not soloFlag:
                            # add newlines, but never more than 1
                            if not newline or line != '\n':
                                newF.write(line)
                            newline = True if line == '\n' else False
                    # if all items removed, just print rest of file
                    else:
                        newF.write(line)
            newF.close()
