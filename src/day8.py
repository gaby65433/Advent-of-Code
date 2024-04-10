from math import lcm

text = open('../inputs/day8.txt','r').read()

def parse_data(text):
    rl,nodes = text.split('\n\n')
    insts = [inst for inst in rl]
    d = {}
    nodes = nodes.split('\n')
    nodes.pop()
    for line in nodes:
        node,ops = line.split('=')
        node,ops = node.strip(),ops.strip()
        ops = ops.replace('(','').replace(')','').replace(' ','')
        left,right = ops.split(',')
        d[node] = (left,right)
    return d,insts

def starting_nodes(lnodes):
    start = []
    for node in lnodes:
        if(node[2] == 'A'):
            start.append(node)
    return start

def part1(lnodes,insts):
    tot = 0
    i = 0
    node = 'AAA'
    while(node != 'ZZZ'):
        tot += 1
        inst = insts[i]
        i += 1
        if (i == len(insts)):
            i = 0
        direction = 0 if inst == 'L' else 1
        node = lnodes[node][direction]
    return tot

def part2(lnodes,insts,start_nodes):
    tot = 1
    for start in start_nodes:
        steps = 0
        i = 0
        while not start.endswith('Z'):
            steps += 1
            inst = insts[i]
            i += 1
            if (i == len(insts)):
                i = 0
            direction = 0 if inst == 'L' else 1
            start = lnodes[start][direction]
        tot = lcm(tot,steps)
    
    return tot

lnodes,insts = parse_data(text)
start_nodes = starting_nodes(lnodes)

print("Part 1:",part1(lnodes,insts))
print("Part 2:",part2(lnodes,insts,start_nodes))