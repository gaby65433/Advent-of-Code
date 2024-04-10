import heapq
import time

text = open('../inputs/day17.txt','r').read()

test_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

def parse_input(text):
    mapa = []
    for line in text.split('\n'):
        if len(line) > 0:
            aux = []
            for elem in line:
                aux.append(int(elem))
            mapa.append(aux)
    return mapa


def valid(x,y,mx,my):
    if (x >=0 and y >= 0 and y<my and x<mx):
        return True
    return False

def travel(mapa,minc,maxc):
    heap = [(mapa[0][1],0,1,1,1),(mapa[1][0],1,0,0,1)] # y,x,dir (0 if facing down,1 if rigth, 2 if up 3 if left), count (travel on same line count), heat cost
    visited = {(0,1,1,1),(1,0,0,1)}
    my,mx = len(mapa),len(mapa[0])
    ops = [(1,0),(0,1),(-1,0),(0,-1)]

    while heap:
        cost,y,x,d,count = heapq.heappop(heap)
        if (y,x) == (my-1,mx-1) and count >= minc:
            return cost

        if count<minc:
            new_y,new_x = y+ops[d][0],x+ops[d][1]
            if not valid(new_x,new_y,mx,my):
                continue
            new_cost = cost + mapa[new_y][new_x]
            if (new_y,new_x,d,count+1) not in visited:
                heapq.heappush(heap, (new_cost, new_y, new_x, d, count + 1))
                visited.add((new_y, new_x, d, count + 1))
        else:
            for i,(opy,opx) in enumerate(ops):
                if opx + ops[d][1] == 0 and opy + ops[d][0] == 0:
                    continue
                new_x = x + opx
                new_y = y + opy
                if count == maxc and i == d or not valid(new_x,new_y,mx,my):
                    continue
                new_cost = cost + mapa[new_y][new_x]
                if d == i:
                    new_count = count + 1
                else:
                    new_count = 1
                if (new_y,new_x,i,new_count) not in visited:
                    heapq.heappush(heap,(new_cost,new_y,new_x,i,new_count))
                    visited.add((new_y,new_x,i,new_count))

def solution(text,minc,maxc):
    mapa = parse_input(text)
    return travel(mapa,minc,maxc)


start_time = time.time_ns() / 1000000
result = solution(text,0,3)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = solution(text,4,10)
end_time = time.time_ns() / 1000000
print(f"Part 2: {result} in {end_time-start_time:.2f} ms")