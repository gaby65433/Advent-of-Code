import time

text = open('../inputs/day16.txt','r').read()

test_input = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

def parse_input(text):
    mapa = []
    for line in text.split('\n'):
        if len(line) > 0:
            aux = []
            for elem in line:
                aux.append(elem)
            mapa.append(aux)
    return mapa

def part1(text):
    mapa = parse_input(text)
    visited = {}
    current = [(0,0,1,0)]
    return travel_v2(mapa,visited,current)

def part2(text):
    mapa = parse_input(text)
    start_pos = [[(0,x) for x in range(len(mapa[0]))],[(y,0) for y in range(len(mapa))],
                 [(len(mapa)-1,x) for x in range(len(mapa[0]))],[(y,len(mapa[0])-1) for y in range(len(mapa))]]
    results = []
    for i,start in enumerate(start_pos):
        if (i == 0):
            dx,dy = 0,1
        elif (i == 1):
            dx,dy = 1,0
        elif (i == 2):
            dx,dy = 0,-1
        else:
            dx,dy = -1,0
        for pos in start:
            y,x = pos
            visited =  {}
            current = [(x,y,dx,dy)]
            results.append(travel_v2(mapa,visited,current)
                           )
    return max(results)
       

def travel_v2(mapa,visited,current):
    while len(current) != 0:
        x,y,dx,dy = current[-1]
        if y<0  or y >= len(mapa) or x<0 or x >=len(mapa[0]):
            current.pop()
        else:
            if (y,x) not in visited:
                visited[(y,x)] = (dx,dy)
            else:
                if visited[(y,x)] == (dx,dy):
                    current.pop()
                    continue
            if mapa[y][x] == '.':
                y += dy
                x += dx
                new = (x,y,dx,dy)
                current[-1] = new
            elif mapa[y][x] == '/':
                if dx != 0:
                    dy = -dx
                    dx = 0
                else:
                    dx = -dy
                    dy = 0
                y += dy
                x += dx
                new =(x,y,dx,dy)
                current[-1] = new
            elif mapa[y][x] == '\\':
                if dx != 0:
                    dy = dx
                    dx = 0
                else:
                    dx = dy
                    dy = 0
                y += dy
                x += dx
                new =(x,y,dx,dy)
                current[-1] = new
            elif mapa[y][x] == '-':
                if dx != 0:
                    x += dx
                    y += dy
                    new = (x,y,dx,dy)
                    current[-1] = new
                else:
                    dy = 0
                    new1 = (x-1,y,-1,dy)
                    new2 = (x+1,y,1,dy)
                    current[-1] = new1
                    current.append(new2)
            else:
                if dy != 0:
                    x += dx
                    y += dy
                    new = (x,y,dx,dy)
                    current[-1] = new
                else:
                    dx = 0
                    new1 = (x,y-1,dx,-1)
                    new2 = (x,y+1,dx,1)
                    current[-1] = new1
                    current.append(new2)

    return len(visited)

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2: {result} in {end_time-start_time:.2f} ms")
    