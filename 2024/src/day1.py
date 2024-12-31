import numpy as np
import time

text = open('../inputs/day1.txt','r').read()

test_input = """3   4
4   3
2   5
1   3
3   9
3   3
"""

def parse_input(text):
    lines = list(map(int,text.replace('\n','   ').split("   ")[:-1]))
    return lines[0:][0::2],lines[1:][0::2]

def part1(text):
    left,right = parse_input(text)

    tot = 0
    while len(left) > 0:
        tot += np.abs(left.pop(left.index(min(left))) - right.pop(right.index(min(right))))

    return tot 

def part2(text):
    left,right = parse_input(text)

    for i in range(len(left)):
        val = left[i]
        left[i] = val * len([i for i in range(len(right)) if right[i] == val])

    return sum(left)

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")