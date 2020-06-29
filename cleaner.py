from helper import solo, comma

def clean(u, fn, fc):
    nums, numItems = [], []
    for _ in range(fc):
        nums.append({})
        numItems.append(0)

    for key, value in u.items():
        x, y = key.split(), value.split()[2:]
        rule = x[0]
        ind = fn.index(x[2])
        for i in range(len(y)):
            if y[i][-1:] == ',':
                nums[ind][int(y[i][:-1])] = rule
            else:
                nums[ind][int(y[i])] = rule
            numItems[ind] += 1

    for i in range(fc):
        nums[i] = sorted(nums[i].items())
        index = 0
        file = fn[i]
        with open(file) as f:
            new = file[:-4] + '-clean.css'
            print(f'Wrote {new}')

            with open(new, 'w') as newF:
                soloFlag, mediaFlag, multiFlag, newline = False, False, False, False
                for num, line in enumerate(f, 1):
                    if index < numItems[i]:
                        if num == nums[i][index][0]:
                            x = solo(line)
                            soloFlag = x
                            multiFlag = not(x)
                        if multiFlag:
                            l = line.split()
                            ll = len(l)
                            for word in l:
                                if comma(word) == nums[i][index][1] or word == nums[i][index][1]:
                                    l.remove(word)
                            ll = len(l)
                            if l[ll - 1] == '{':
                                l[ll - 2] = comma(l[ll - 2])
                            else:
                                l[ll - 1] = comma(l[ll - 1])
                            line = ' '.join(l) + '\n'
                            index += 1
                            multiFlag = False
                        if line[:6] == '@media':
                            mediaFlag = True
                        if soloFlag:
                            for c in line:
                                if c == '}':
                                    soloFlag = False
                                    index += 1
                        elif not soloFlag:
                            if not newline or line != '\n':
                                newF.write(line)
                            newline = True if line == '\n' else False
                if mediaFlag:
                    newF.write('}')
            newF.close()
