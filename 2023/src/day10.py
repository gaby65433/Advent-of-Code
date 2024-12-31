import time
from datetime import timedelta

text = open('../inputs/day10.txt','r').read()


paths = {'|':[(1,0),(-1,0)],'-':[(0,1),(0,-1)],'L':[(-1,0),(0,1)],
         'J':[(0,-1),(-1,0)],'7':[(0,-1),(1,0)],'F':[(0,1),(1,0)]}

possible = [(-1,0),(0,-1),(0,1),(1,0)]


def parse(text):
    mapa = []
    for i,line in enumerate(text.split('\n')):
        if len(line) > 0:  
            aux = []
            for j,elem in enumerate(line):
                aux.append(elem)
                if elem == 'S':
                    start_pos = (i,j)
            mapa.append(aux)

    return mapa,start_pos


def connected(symbol,old_i,old_j,new_i,new_j):
    if symbol not in paths:
        return False
    p = paths[symbol]
    for i,j in p:
        ii,jj = new_i + i, new_j+j
        if ii == old_i and jj == old_j:
            return True
    return False

def part1(mapa,start_pos):
    visited = set()
    sl,sc = start_pos
    current = set()
    for i,j in possible:
        new_l,new_c = sl+i,sc+j
        if (new_l) >= len(mapa) or (new_l) < 0 or (new_c) >= len(mapa[i]) or (new_c) < 0:
                pass
        elif (connected(mapa[new_l][new_c],sl,sc,new_l,new_c) and (new_l,new_c) not in visited):
            visited.add((new_l,new_c))
            current.add((new_l,new_c))
            cl,cc = new_l,new_c
            break
    previous = (sl,sc)

    while (sl,sc) not in current:
        for i,j in paths[mapa[cl][cc]]:
            new_l, new_c = cl +i, cc + j
            if (new_l) >= len(mapa) or (new_l) < 0 or (new_c) >= len(mapa[i]) or (new_c) < 0 or previous == (new_l,new_c):
                continue
            visited.add((new_l,new_c))
            current.add((new_l,new_c))
            previous = (cl,cc)
            cl,cc = new_l,new_c
            break

    return len(current) //2,visited


def part2(visited,mapa):
    tot = 0
    ig = ""
    for l in range(len(mapa)):
        inside = False
        for c in range(len(mapa[l])):
            if (l, c) in visited:
                if mapa[l][c] in {"F"}:
                    ig = "7"
                elif mapa[l][c] in {"L"}:
                    ig = "J"
                elif mapa[l][c] in {"-"}:
                    continue
                else:
                    if mapa[l][c] != ig:
                        inside = not inside
                    ig = ""
            elif inside:
                tot += 1
    return tot

mapa,start_pos = parse(text)

start_time = time.time_ns() / 1000000
result, visited = part1(mapa,start_pos)
end_time = time.time_ns() / 1000000
print(f"Parte 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(visited,mapa)
end_time = time.time_ns() / 1000000
print(f"Parte 2: {result} in {end_time-start_time:.2f} ms")