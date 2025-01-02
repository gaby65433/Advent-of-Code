from functools import cmp_to_key
import time

text = open('../inputs/day6.txt','r').read()

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

directions = {"^":(-1,0), "v":(1,0), "<":(0,-1), ">":(0,1)}

def turn_right(pos, grid):
    match grid[pos]:
        case "^":
            return (pos[0], pos[1]+1)
        case "v":
            return (pos[0], pos[1]-1)
        case "<":
            return (pos[0]-1, pos[1])
        case ">":
            return (pos[0]+1, pos[1])
        case _:
            return pos

def part1(text):
    lines = text.splitlines()
    h, w = len(lines), len(lines[0])
    grid = {(y, x): lines[y][x] for y in range(h) for x in range(w)}

    pos = list(filter(lambda x: x[1] == "^", list(grid.items())))[0][0]
    visited = {}
    inside = True

    while inside:
        if pos not in visited:
            visited[pos] = grid[pos]
        direction = directions[grid[pos]]
        newpos = (pos[0] + direction[0], pos[1] + direction[1])

        if grid.get(newpos) is None:
            inside = False
        else:
            if grid.get(newpos) == "#":
                newpos = turn_right(pos, grid)
                grid[pos] = "^" if grid[pos] == "<" else "<" if grid[pos] == "v" else "v" if grid[pos] == ">" else ">"
            grid[newpos] = grid[pos]
            grid[pos] = "X"
            pos = newpos

    return len(visited),visited

def part2(text):
    """Far from optimal, but it works
       Added little optimization, starting the search in the position rigth before placing the new obstacle
    """

    tot = 0
    lines = text.splitlines()
    h, w = len(lines), len(lines[0])
    original_grid = {(y, x): lines[y][x] for y in range(h) for x in range(w)}

    _,possibilities = part1(text)

    for (y,x),start in possibilities.items():
            grid = original_grid.copy()
            init = list(filter(lambda l: l[1] == "^", list(grid.items())))[0][0]
            grid[init] = "."
            grid[(y, x)] = "#"

            if start == "^":
                pos = (y+1, x)
                grid[pos] = ">"
            elif start == "v":
                pos = (y-1, x)
                grid[pos] = "<"
            elif start == "<":
                pos = (y, x+1)
                grid[pos] = "^"
            elif start == ">":
                pos = (y, x-1)
                grid[pos] = "v"
   
            visited = set()
            inside = True

            while inside:
                visited.add((pos, grid[pos]))
                direction = directions[grid[pos]]
                newpos = (pos[0] + direction[0], pos[1] + direction[1])
                if grid.get(newpos) is None:
                    inside = False
                else:
                    if grid.get(newpos) == "#":
                        while grid.get(newpos) == "#":
                            newpos = turn_right(pos, grid)
                            grid[pos] = "^" if grid[pos] == "<" else "<" if grid[pos] == "v" else "v" if grid[pos] == ">" else ">"
                    
                    grid[newpos] = grid[pos]
                    grid[pos] = "X"
                    pos = newpos
                    if (newpos, grid[newpos]) in visited:
                        inside = False
                        tot+=1

    return tot

start_time = time.time_ns() / 1000000
result,_ = part1(test_input)
end_time = time.time_ns() / 1000000
print(f"Part 1: {result} in {end_time-start_time:.2f} ms")

start_time = time.time_ns() / 1000000
result = part2(text)
end_time = time.time_ns() / 1000000
print(f"Part 2 : {result} in {end_time-start_time:.2f} ms")