from helper import solo, comma

def clean(u, fn, fc):
    # pre-populate arrays
    nums = [{}] * fc
    numItems = [0] * fc

    # extract line numbers, filenames
    for key, value in u.items():
        k, v = key.split(), value.split()[2:]
        rule = k[0]
        ind = fn.index(k[2])
        # for each line number
        for i in range(len(v)):
            nums[ind][int(comma(v[i]))] = rule
            numItems[ind] += 1

    # for each file
    for i in range(fc):
        # sort by line number
        nums[i] = sorted(nums[i].items())
        index, file = 0, fn[i]
        with open(file) as f:
            new = file[:-4] + '-clean.css'
            print(f'Wrote {new}')

            # open new file to write
            with open(new, 'w') as newF:
                soloFlag, mediaFlag, multiFlag, newline = False, False, False, False
                for num, line in enumerate(f, 1):
                    # if haven't yet removed all items
                    if index < numItems[i]:
                        # if line has an unused rule
                        if num == nums[i][index][0]:
                            x = solo(line)
                            soloFlag = x
                            multiFlag = not(x)
                        # if multiple rules
                        if multiFlag:
                            l = line.split()
                            ll = len(l)
                            for word in l:
                                # remove unused rules
                                if comma(word) == nums[i][index][1] or word == nums[i][index][1]:
                                    l.remove(word)
                            ll = len(l)
                            # adjust commas based on presence of opening brace
                            if l[ll - 1] == '{':
                                l[ll - 2] = comma(l[ll - 2])
                            else:
                                l[ll - 1] = comma(l[ll - 1])
                            line = ' '.join(l) + '\n'
                            index += 1
                            multiFlag = False
                        # if media query opening
                        if line[:6] == '@media':
                            mediaFlag = True
                        # if one rule
                        if soloFlag:
                            for c in line:
                                # ignore until rule closes
                                if c == '}':
                                    soloFlag = False
                                    index += 1
                        elif not soloFlag:
                            # add newlines, but never more than 1
                            if not newline or line != '\n':
                                newF.write(line)
                            newline = True if line == '\n' else False
                # bandage, add closing brace to media query
                if mediaFlag:
                    newF.write('}')
            newF.close()
