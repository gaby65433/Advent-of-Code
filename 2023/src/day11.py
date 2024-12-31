import time

text = open('../inputs/day11.txt','r').read()
lines = text.split('\n')

def parse_data(lines):
    stars = []
    csize = len(lines)
    if len(lines[-1]) == 0:
        csize-=1
    auxc = [1 for _ in range(csize)]
    auxl = [1 for _ in range(len(lines[0]))]
    for i,line in enumerate(lines):
        if len(line) > 0:
            for j,elem in enumerate(line):
                if (elem == '#'):
                    auxl[i] = 0
                    auxc[j] = 0
                    stars.append((i,j))
            
    return stars,auxl,auxc

def solution(loc,l,c,expansion=1):
    tot = 0
    for i in range(len(loc)):
        j = i+1
        ls,cs = loc[i]
        while(j<len(loc)):
            line,colum = loc[j]
            lmin,lmax = min(line,ls),max(line,ls)
            cmin,cmax = min(colum,cs),max(colum,cs)
            tot += abs(line-ls) + sum(l[lmin:lmax]) * (expansion-1) + abs(colum-cs) + sum(c[cmin:cmax]) * (expansion - 1)
            j += 1

    return tot
start_time = time.time_ns() / 1000
stars,l,c = parse_data(lines)
end_time = time.time_ns() / 1000
print(f"Parsing done in {end_time-start_time:.2f} us")

start_time = time.time_ns() / 1000000
result = solution(stars,l,c,2)
end_time = time.time_ns() / 1000000
print(f"Parte 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = solution(stars,l,c,1000000)
end_time = time.time_ns() / 1000000
print(f"Parte 2: {result} in {end_time-start_time:.2f} ms")

        
