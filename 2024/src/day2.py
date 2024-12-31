import numpy as np
import time

text = open('../inputs/day2.txt','r').read()

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def errors(levels, bad_allowed = False):
    if not bad_allowed:       
        sig = levels[0] - levels[1]
        if np.abs(sig) <1 or np.abs(sig) >3:
            return False
        for i in range(1,len(levels)-1):
            val = levels[i] - levels[i+1]
            if np.abs(val) <1 or np.abs(val) >3 or val * sig <= 0:
                return False

    else:
        sig = levels[0] - levels[1]
        if np.abs(sig) <1 or np.abs(sig) >3:
            return True in [errors(levels[1:],False),errors([levels[0]]+levels[2:],False)]
        for i in range(1,len(levels)-1):
            val = levels[i] - levels[i+1]
            if np.abs(val) <1 or np.abs(val) >3 or val * sig <= 0:
                return True in [errors(levels[0:i]+levels[i+1:],False),errors(levels[0:i+1]+levels[i+2:],False),errors(levels[1:],False),errors([levels[0]]+levels[2:],False)]
            
    return True

def part1(text):
    reports = text.splitlines()

    errorL = []
    for report in reports:
        levels = list(map(int,report.split()))
        errorL.append(errors(levels))

    safe = len(list(filter(lambda x: x, errorL)))

    return safe

def part2(text):
    reports = text.splitlines()

    errorL = []
    for report in reports:
        levels = list(map(int,report.split()))
        errorL.append(errors(levels,bad_allowed=True))

    safe = len(list(filter(lambda x: x, errorL)))

    return safe

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")