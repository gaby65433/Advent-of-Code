import time
import copy
import numpy as np

text = open('../inputs/day14.txt','r').read()

test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

def north(lines):
    for ind,line in enumerate(lines):
        if len(line) > 0:
            for j,elem in enumerate(line):
                if elem == 'O':
                    aux = ind
                    while aux - 1 >= 0 and lines[aux-1][j] == '.':
                        lines[aux][j],lines[aux-1][j] = lines[aux-1][j],lines[aux][j]
                        aux -= 1
    return lines

def south(lines):
    for i in range(len(lines)-1,-1,-1):
        if (len(lines[i]) > 0):
            for j,elem in enumerate(lines[i]):
                if elem == 'O':
                    aux = i
                    while aux + 1 < len(lines) and lines[aux+1][j] == '.':
                        lines[aux][j],lines[aux+1][j] = lines[aux+1][j],lines[aux][j]
                        aux += 1
    return lines


def west(lines):
    for line in lines:
        if len(line) > 0:
            for j,elem in enumerate(line):
                if elem == 'O':
                    aux = j
                    while aux - 1 >= 0 and line[aux-1] == '.':
                        line[aux],line[aux-1] = line[aux-1],line[aux]
                        aux -= 1
    return lines

def east(lines):
    for line in lines:
        if len(line) > 0:
            for j in range(len(line)-1,-1,-1):
                if line[j] == 'O':
                    aux = j
                    while aux + 1 <len(line) and line[aux+1] == '.':
                        line[aux],line[aux+1] = line[aux+1],line[aux]
                        aux += 1
    return lines

def solution(text,maximum = 0):
    tot = 0
    lines = text.splitlines()
    for i,line in enumerate(lines):
        line =list(line)
        lines[i] = line

    cycle = []
    
    for k in range(maximum):

        lines = north(lines)
        lines = west(lines)
        lines = south(lines)
        lines = east(lines)

        if lines in cycle:
            break
        
        cycle.append(copy.deepcopy(lines))

         
    if maximum == 0:
        lines = north(lines)
    else:
        occor = cycle.index(lines)
        periode = k - occor
        ind = (maximum-occor) % periode + occor - 1
    
        lines = cycle[ind]

    for ind,line in enumerate(lines):
        mult = len(lines) - ind
        for elem in line:
            if elem == 'O':
                tot += mult

    return tot

start_time = time.time_ns() / 1000000
result = solution(text)
end_time = time.time_ns() / 1000000
print(f"Parte 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = solution(text,1000000000)
end_time = time.time_ns() / 1000000
print(f"Parte 2: {result} in {end_time-start_time:.2f} ms")

