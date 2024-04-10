import re

text = open('../inputs/day4.txt','r').read()

lines = text.split('\n')


def part1(lines):
    tot = 0
    for line in lines:
        if len(line) > 1:
            local_tot = 0
            i = 0
            cards = line.split(':')[1]
            temp = cards.split('|')
            Wcards,PCards = temp[0].strip(),temp[1].strip()
            Wcards = re.sub(r' +',' ',Wcards).split(' ')
            PCards = re.sub(r' +',' ',PCards).split(' ')
            for card in PCards:
                if card in Wcards:
                    if i == 0:
                        local_tot = 1
                        i += 1
                    else:
                        local_tot *= 2
            tot += local_tot

    return tot

def part2(lines):
    total = 0
    tot = {}
    for line in lines:
        if len(line) > 1:
            i = 1
            id = int(line.split(':')[0].replace(' ','').split('Card')[1])
            tot[id] = tot.get(id,0) + 1
            cards = line.split(':')[1]
            temp = cards.split('|')
            Wcards,PCards = temp[0].strip(),temp[1].strip()
            Wcards = re.sub(r' +',' ',Wcards).split(' ')
            PCards = re.sub(r' +',' ',PCards).split(' ')
            for card in PCards:
                if card in Wcards:
                    tot[id+i] = tot.get(id+i,0) + 1 * tot[id]
                    i+= 1
    
    return sum(tot.values())

print(part1(lines))
print(part2(lines))
