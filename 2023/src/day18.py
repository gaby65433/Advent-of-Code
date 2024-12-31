import heapq
import time

text = open('../inputs/day18.txt','r').read()

test_input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

def part1(text):
    currentx = 0
    currenty = 0
    border = 0
    area = 0
    previous = (0,8)
    for line in text.splitlines():
        if len(line) > 0:
            d,distance,code = line.split()
            border += int(distance)
            previous,area,currentx,currenty = add_area(area,previous,d,currentx,currenty,int(distance))
    
    area += border

    return (area // 2) + 1 

def part2(text):
    directions = {'0':'R','1':'D','2':'L','3':'U'}
    currentx = 0
    currenty = 0
    points = [(0,0)]
    border = 0
    area = 0
    previous = (0,0)
    for line in text.splitlines():
        if len(line) > 0:
            d,distance,code = line.split()
            code = code.strip('()').replace("#","0x")
            distance,d = int(code[0:7],0),directions[code[-1]]
            border += int(distance)
            if (d == 'R'):
                for i in range(int(distance)):
                    currentx += 1
                    area += previous[1] * currenty - currentx * previous[0]
                    previous = (currenty,currentx)


            elif (d == 'L'):
                for i in range(int(distance)):
                    currentx -= 1
                    area += previous[1] * currenty - currentx * previous[0]
                    previous = (currenty,currentx)


            elif (d == 'U'):
                for i in range(int(distance)):
                    currenty -= 1
                    area += previous[1] * currenty - currentx * previous[0] 
                    previous = (currenty,currentx)

            elif (d == 'D'):
                for i in range(int(distance)):
                    currenty += 1
                    area += previous[1] * currenty - currentx * previous[0] 
                    previous = (currenty,currentx)

    area += border

    return (area // 2) + 1 


def add_area(area,previous,d,currentx,currenty,distance):
    if (d == 'R'):
        currentx += distance
        area += previous[1] * currenty - currentx * previous[0]
        previous = (currenty,currentx)
    elif (d == 'L'):
            currentx -= int(distance)
            area += previous[1] * currenty - currentx * previous[0]
            previous = (currenty,currentx)
    elif (d == 'U'):
            currenty -= int(distance)
            area += previous[1] * currenty - currentx * previous[0]
            previous = (currenty,currentx)
    elif (d == 'D'):
        currenty += int(distance)
        area += previous[1] * currenty - currentx * previous[0]
        previous = (currenty,currentx)
    return previous,area,currentx,currenty

def part2(text):
    directions = {'0':'R','1':'D','2':'L','3':'U'}
    currentx = 0
    currenty = 0
    border = 0
    area = 0
    previous = (0,0)
    for line in text.splitlines():
        if len(line) > 0:
            d,distance,code = line.split()
            code = code.strip('()').replace("#","0x")
            distance,d = int(code[0:7],0),directions[code[-1]]
            border += int(distance)
            previous,area,currentx,currenty = add_area(area,previous,d,currentx,currenty,int(distance))

    area += border

    return (area // 2) + 1 

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")