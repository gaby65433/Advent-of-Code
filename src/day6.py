import re
import math
text = open('../inputs/day6.txt','r').read()



def part1(text):
    total = []
    lines = list(filter(lambda y: y!= None,map(lambda x: x.split(':')[1].strip() if (len(x) >1) else None ,text.split('\n'))))
    lines = list(map(lambda l: l.split(' ') ,list(map(lambda x: re.sub(r' +',' ',x),lines))))
    games = []
    for i in range(len(lines[0])):
        games.append((int(lines[0][i]),int(lines[1][i])))

    for game in games:
        wins = 0
        time,record = game[0],game[1]
        for hold_time in range(1,time+1):
            vel = hold_time
            dist = vel * (time-hold_time)
            if (dist > record):
                wins += 1

        total.append(wins)

    return math.prod(total)


def part2(text):
    lines = list(filter(lambda y: y!= None,map(lambda x: x.split(':')[1].strip() if (len(x) >1) else None ,text.split('\n'))))
    lines = list(map(lambda l: l.replace(' ','') ,lines))
    games = list(map(lambda x: int(x),lines))
    time,record = games[0],games[1]
    wins = int(math.sqrt(time*time-4*record))

    return wins

print(part1(text))
print(part2(text))