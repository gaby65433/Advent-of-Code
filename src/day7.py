text = open('../inputs/day7.txt','r').read()

vals = {'A' : 13, 'K':12 ,'Q':11 ,'J':10,'T':9}


def valor(char,part=1):
    if(part == 1):
        if char in vals:
            return vals[char]
        else:
            return int(char)-1
    else:
        if char in vals:
            if char == 'J':
                return 1
            elif (char == 'T'):
                return 10
            else:
                return vals[char]
        else:
            return int(char)

def part1(text):
    card_list = {}
    lines = text.split('\n')
    tot = 0
    for line in lines:
        if len(line) > 1:
            cards, bid = line.split(' ')
            d = {}
            for i in cards:
                d[i] = d.get(i,0) + 1
            val = max(d.values())
            if val == 5:
                val = 7
            elif val == 4:
                val = 6
            elif val == 3:
                if len(d) == 2:
                    val = 5
                else:
                    val = 4
            elif val == 2:
                if len(d) == 3:
                    val = 3
                else:
                    val = 2
            if val not in card_list:
                card_list[val] = [(cards,int(bid))]
            else:
                card_list[val].append((cards,int(bid)))

    card_list = dict(sorted(card_list.items()))
    
    for key in card_list:
        card_list[key] = sorted(card_list[key],key = lambda x: Hand_stength(x[0]))

    #print(card_list)
    #print(card_list)
    cont = 1
    for key in card_list:
        for elem in card_list[key]:
            tot += cont * elem[1]
            cont+=1
    return tot


def Hand_stength(hand,part):
    strength = 0
    for index,card in enumerate(hand):
        strength += valor(card,part) * 13 ** (5-index)
    return strength

def part2(text,part):
    card_list = {}
    lines = text.split('\n')
    tot = 0
    for line in lines:
        if len(line) > 1:
            cards, bid = line.split(' ')
            d = {}
            for i in cards:
                d[i] = d.get(i,0) + 1
            
            Js = 0
            if (part == 2):
                if 'J' in d:
                    Js = d.pop('J')
            if d == {}:
                val = Js
            else:
                val = max(d.values()) + Js
            if val == 5:
                val = 7
            elif val == 4:
                val = 6
            elif val == 3:
                if len(d) == 2:
                    val = 5
                else:
                    val = 4
            elif val == 2:
                if len(d) == 3:
                    val = 3
                else:
                    val = 2
            if val not in card_list:
                card_list[val] = [(cards,int(bid))]
            else:
                card_list[val].append((cards,int(bid)))

    card_list = dict(sorted(card_list.items()))
    
    for key in card_list:
        card_list[key] = sorted(card_list[key],key = lambda x: Hand_stength(x[0],part))

    #print(card_list)
    #print(card_list)
    cont = 1
    for key in card_list:
        for elem in card_list[key]:
            tot += cont * elem[1]
            cont+=1
    return tot


print(part2(text,1))
print(part2(text,2))