import time
import copy
import numpy as np

text = open('../inputs/day15.txt','r').read()

test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def part1(text):
    tot = 0
    table =  {}
    for step in text.split(','):
        tot += get_id(step)

    return tot

def get_id(string):
    val = 0
    for elem in string:
        val = ((val + ord(elem)) * 17) % 256
    return val

def part2(text):
    boxes = {_:{} for _ in range(256)}
    for step in text.split(','):
        if step[-2] == '=':
            label,lens= step.split("=")
            box_id = get_id(label)
            boxes[box_id][label] = int(lens)
        else:
            label = step[:len(step)-1]
            box_id = get_id(label)
            if label in boxes[box_id]:
                boxes[box_id].pop(label)

    return sum(sum((i+1) * (j+1) * lens for j,lens in enumerate(box.values())) for i,box in enumerate(boxes.values()))
            
start_time = time.time_ns() / 1000000
result = part1(text)
end_time = time.time_ns() / 1000000
print(f"Parte 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Parte 2: {result} in {end_time-start_time:.2f} ms")