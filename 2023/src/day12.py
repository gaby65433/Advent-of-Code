import time

text = open('../inputs/day12.txt','r').read()

test_input = """
?#?#?#?#?#?#?#? 1,3,1,6
.??..??...?##. 1,1,3
???.### 1,1,3
?###???????? 3,2,1
????.######..#####. 1,6,5
????.#...#... 4,1,1
"""

def check_spring_not_working_shit(spring,combs):
    
    if len(spring) == 0 and len(combs) == 0:
        return 1
    elif len(spring) > 0 and len(combs) == 0:
        return int(all(x != '#' for x in spring))
    elif len(spring) == 0 and len(combs) > 0:
        return 0

    combs1 = combs.copy()
    combs2 = combs.copy()
    spring1 = spring.copy()
    spring2 = spring.copy()

    if spring[0] == '.':
        spring1.pop(0)
        return check_spring_not_working_shit(spring1,combs1)
    
    elif spring[0] == '?':
        spring1[0] = '.'
        spring2[0] = '#'
        return check_spring_not_working_shit(spring1,combs1) + check_spring_not_working_shit(spring2,combs2)

    else:
        jump = 0
        for i in range(combs1[0]):
            if i >= len(spring):
                spring1.pop(0)
                return 0
            else:
                jump += 1
                if spring[i] == '.':
                    spring1.pop(0)
                    return 0

        combs1.pop(0)
        for _ in range(jump):
            spring1.pop(0)
        
        if len(spring1) > 0:
            x = spring1.pop(0)
            if x == '#':
                return 0

        return check_spring_not_working_shit(spring1,combs1)


def check_spring(l,r):
    done = {}
    def permut(i,j):
        if (i,j) in done:
            return done[(i,j)]
        if i == 0 and j == 0:
            return 1
        elif i == 0:
            return 0
        elif j == 0:
            return int(all(x != '#' for x in l[:i]))
        elif l[i-1] == '.':
            answer = permut(i-1,j)
        else:
            num = r[j-1]
            if num > i or any(x == '.' for x in l[i-num:i]):
                answer = 0
            elif i > num and l[i-num-1] == '#':
                answer = 0
            else:
                answer = permut(max(i-num-1,0),j-1)
            if l[i-1] == '?':
                answer += permut(i-1,j)
        done[(i,j)] = answer
        return answer
    return permut(len(l),len(r))
    

def part1(data):
    tot = 0
    lines = data.split('\n')
    for line in lines:
        if len(line) > 0:
            springs, combs = line.split()
            combs = list(map(lambda x: int(x), combs.split(',')))
            springs = [x for x in springs]
            tot += check_spring_not_working_shit(springs,combs)  
    
    return tot            

def solution(data):
    tot1 = 0
    tot2 = 0
    lines = data.split('\n')
    for line in lines:
        if len(line) > 0:
            springs, combs = line.split()
            s1 = springs
            s2 = '?'.join([springs]*5)
            c1 = tuple(map(lambda x: int(x), combs.split(',')))
            c2 = c1 * 5
            tot1 += check_spring(s1,c1)
            tot2 += check_spring(s2,c2)
    
    return tot1,tot2

start_time = time.time_ns() / 1000000
result1,result2 = solution(text)
end_time = time.time_ns() / 1000000

print(f"Part 1: {result1} in {end_time-start_time:.2f} ms")
print(f"Part 2: {result2} in {end_time-start_time:.2f} ms")
