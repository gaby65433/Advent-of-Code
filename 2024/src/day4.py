import numpy as np
import time

text = open('../inputs/day4.txt','r').read()

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def part1(text):

    lines = text.splitlines()

    tot = 0
    h, w = len(lines), len(lines[0])
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    moves = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    target = "XMAS"

    for y,x in grid:
        for dy,dx in moves:
            word = "".join([grid.get((y+i*dy,x+i*dx),"") for i in range(len(target))])
            tot += word == target

    return tot
            

def part2(text):

    lines = text.splitlines()

    tot = 0
    h, w = len(lines), len(lines[0])
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    for y,x in grid:
        if lines[y][x] == "A":
            word1 = grid.get((y-1,x-1),"") + grid.get((y+1,x+1),"")
            word2 = grid.get((y-1,x+1),"") + grid.get((y+1,x-1),"")
            tot += {word1, word2} <= {"MS", "SM"}

    return tot

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")