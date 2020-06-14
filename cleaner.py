from helper import solo, comma

def clean(u):
    nums = {}
    file = ''
    for key, value in u.items():
        x, y = key.split(), value.split()
        rule, file = x[0], x[2]

        for i in range(len(y) - 2):
            if y[i+2][-1:] == ',':
                nums[int(y[i+2][:-1])] = rule
            else:
                nums[int(y[i+2])] = rule

    nums = sorted(nums.items())
    numItems = len(nums)
    index = 0

    with open(file) as f:
        print(f'Cleaned {file}')

        with open(file[:-4] + '-clean.css', 'w') as newF:
            soloFlag, mediaFlag, multiFlag = False, False, False
            for num, line in enumerate(f, 1):
                if index < numItems:
                    if num == nums[index][0]:
                        x = solo(line)
                        if x:
                            soloFlag = True
                        if not x:
                            multiFlag = True
                            l = line.split()
                            ll = len(l)
                    if multiFlag:
                        for word in l:
                            cWord = comma(word)
                            if cWord == nums[index][1]:
                                l.remove(cWord)
                            elif word == nums[index][1]:
                                l.remove(word)
                        ll = len(l)
                        if l[ll - 1] == '{':
                            l[ll - 2] = comma(l[ll - 2])
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
                        newF.write(line)
            if mediaFlag:
                newF.write('}')
        newF.close()
