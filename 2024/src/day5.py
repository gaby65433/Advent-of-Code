from functools import cmp_to_key
import time

text = open('../inputs/day5.txt','r').read()

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def part1(text):

    sections = text.split("\n\n")
    rules = sections[0].splitlines()
    rules = [tuple(map(int,line.split('|'))) for line in rules]
    prints = sections[1].splitlines()
    pages = [list(map(int,print_.split(","))) for print_ in prints]

    def compare(a,b):
        if (a, b) in rules:
            return -1
        elif (b,a) in rules:
            return 1
        else:
            return 0

    tot = 0

    for page in pages:
        new = sorted(page, key=cmp_to_key(compare))
        if new == page:
            tot += new[len(new)//2]


    return tot

def part2(text):

    sections = text.split("\n\n")
    rules = sections[0].splitlines()
    rules = [tuple(map(int,line.split('|'))) for line in rules]
    prints = sections[1].splitlines()
    pages = [list(map(int,print_.split(","))) for print_ in prints]

    def compare(a,b):
        if (a, b) in rules:
            return -1
        elif (b,a) in rules:
            return 1
        else:
            return 0

    tot = 0

    for page in pages:
        new = sorted(page, key=cmp_to_key(compare))
        if new != page:
            tot += new[len(new)//2]


    return tot

start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")