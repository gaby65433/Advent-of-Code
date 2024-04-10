import time

text = open('../inputs/day13.txt','r').read()

test_input = """

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

"""
def all_equal(coisa,i,j):
    while(i >= 0 and j<len(coisa)):
        if coisa[i] != coisa[j]:
            return False
        i-=1
        j+=1
    return True


def check_equal(lines):
    for i in range(len(lines)-1):
        if all_equal(lines,i,i+1):
            return i+1
    return 0

def check_equal_v2(lines,target):
    for i in range(len(lines)-1):
        smudge = 0
        for j in range(i+1):
            if i + j + 1 >= len(lines):
                continue

            row1 = lines[i-j]
            row2 = lines[i+j+1]
            for a,b in zip(row1,row2):
                if a != b:
                    smudge += 1
            if smudge == target and all_equal(lines,i-j-1,i+j+2):
                return i+1
    return 0


def part1(text):
    tot = 0
    patterns = text.split('\n\n')
    for pattern in patterns:
        if len(pattern) > 0:
            lines = pattern.splitlines()
            cols = []
            for i in range(len(lines[0])):
                cols.append("".join([row[i] for row in lines]))
                
            tot += check_equal(lines) * 100 + check_equal(cols)
   
    return tot

def part2(text):
    tot = 0
    patterns = text.split('\n\n')
    for pattern in patterns:
        if len(pattern) > 0:
            lines = pattern.splitlines()
            cols = []
            for i in range(len(lines[0])):
                cols.append("".join([row[i] for row in lines]))
                
            tot += check_equal_v2(lines,1) * 100 + check_equal_v2(cols,1)
   
    return tot

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Parte 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Parte 2: {result} in {end_time-start_time:.2f} ms")
