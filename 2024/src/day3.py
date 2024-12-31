import numpy as np
import time

text = open('../inputs/day3.txt','r').read()

test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def part1(text):
    tot = 0
    i = 0
    while i < len(text):
        if text[i:i+4] == 'mul(':
            start = i + 4
            end = text.find(')',i)
            args = ""
            while start != end:
                if text[start] not in ['0','1','2','3','4','5','6','7','8','9',',']:
                    break
                else:
                    args += text[start]
                    start += 1
            if start == end:
                tot += np.prod(list(map(int,args.split(','))))
            i=start
        else:
            i += 1

    return tot

def part2(text):
    enabled = True
    tot = 0
    i = 0
    while i < len(text):
        if text[i:i+4] == "do()":
            enabled = True
            i += 4
        elif text[i:i+7] == "don't()":
            enabled = False
            i += 7
        elif text[i:i+4] == 'mul(' and enabled:
            start = i + 4
            end = text.find(')',i)
            args = ""
            while start != end:
                if text[start] not in ['0','1','2','3','4','5','6','7','8','9',',']:
                    break
                else:
                    args += text[start]
                    start += 1
            if start == end:
                tot += np.prod(list(map(int,args.split(','))))
            i=start
        else:
            i += 1

    return tot

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")