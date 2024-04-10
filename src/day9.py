text = open('../inputs/day9.txt','r').read()

def part1(text):
    tot = 0
    lines = text.split('\n')
    for line in lines:
        if len(line) >1:
            l = [int(x) for x in line.split(' ')]
            tot += l[-1]
            flag = True
            while flag:
                flag = False
                for i in range(0,len(l)-1):
                    x = l[i+1]-l[i]
                    l[i] = x
                    if x != 0:
                        flag = True
                l.pop()
                tot += l[-1]
    return tot

def part2(text):
    tot = 0
    lines = text.split('\n')
    for line in lines:
        mult = 1
        if len(line) >1:
            l = [int(x) for x in line.split(' ')]
            tot += l[0] * mult
            mult *= -1
            flag = True
            while flag:
                flag = False
                for i in range(0,len(l)-1):
                    x = l[i+1]-l[i]
                    l[i] = x
                    if x != 0:
                        flag = True
                l.pop()
                tot += l[0]*mult
                mult *= -1
    return tot

print("Part 1:",part1(text))
print("Part 2:",part2(text))