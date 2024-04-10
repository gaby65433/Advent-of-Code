text = open('../inputs/day2.txt','r').read()

lines = text.split('\n')


def possible_1(lines,rmax,gmax,bmax):
    tot = 0
    for line in  lines:
        if(len(line)<1): 
            continue
        possible = True
        id = line.split(':')[0].split(' ')[1]
        trows = line.split(':')[1].split(';')
        for trow in trows:
            single = trow.split(',')
            for elem in single:
                x = elem.strip().split(' ')
                match x[1]:

                    case 'red':
                        if possible and int(x[0]) > rmax:
                            possible = False

                    case 'blue':
                        if possible and int(x[0]) > bmax:
                            possible = False

                    case 'green':
                        if possible and int(x[0]) > gmax:
                            possible = False
        if possible:
            tot += int(id)
    return tot

def possible_2(lines):
    tot = 0
    for line in  lines:
        if(len(line)<1): 
            continue
        trows = line.split(':')[1].split(';')
        mred = 0
        mblue = 0
        mgreen = 0
        for trow in trows:
            single = trow.split(',')
            for elem in single:
                x = elem.strip().split(' ')
                match x[1]:

                    case 'red':
                        if int(x[0]) > mred:
                            mred = int(x[0])

                    case 'blue':
                        if int(x[0]) > mblue:
                            mblue = int(x[0])

                    case 'green':
                        if int(x[0]) > mgreen:
                            mgreen = int(x[0])

        tot += mred*mgreen*mblue
    return tot

print(possible_1(lines,12,13,14))
print(possible_2(lines))
