text = open('../inputs/day3.txt','r').read()

lines = text.split('\n')

def create_map(lines):
    map = []
    for line in lines:
        l = []
        for i,elem in enumerate(line):
            l.append((elem,False))
        if(l!=[]):
            map.append(l)
    return map

def check_neighbour(map,line,start,end,case):
    for l in range(line-1,line+2):
        for i in range(start-1,end+2):
            if (l<0 or l>len(map)-1 or i<0 or i>len(map[0])-1):
                continue
            if(case == 1):
                if (map[l][i][0] != '.' and (not(map[l][i][0].isdigit()))):
                    return True,(l,i)
            else:
                if (map[l][i][0] == '*' and map[l][i][1] == False):
                    map[l][i] = tuple([map[l][i][0],True])
                    return True,(l,i)

    return False,(l,i)


def adjacent(lines,case):
    map = create_map(lines)
    tot = 0
    for i,line in enumerate(map):
        s = ''
        j = 0
        while j < len(line):
            start = j
            while j < len(line) and line[j][0].isdigit():
                s += line[j][0]
                j+=1

            if(s != ''):
                flag,pair = check_neighbour(map,i,start,j-1,case)
                if (case == 1):
                    if(flag == True):
                        tot += int(s)
                else:
                    y,x = pair[0],pair[1]
                    if(flag == True):
                        found,count = check_for_numbers(map,x,y)
                        if (count == 2):
                            tot += int(found[0])*int(found[1])
                s = ''

            else:
                j+= 1

    return tot

def check_for_numbers(map,x,y):
    cont = 0
    l = y-1
    found = []
    while l<y+2:
        i = x-1
        while i<x+2:
            if (l<0 or l>len(map)-1 or i<0 or i>len(map[0])-1):
                continue
            
            if map[l][i][0].isdigit():
                s = map[l][i][0]
                cont += 1
                i_min_temp = i-1
                i_max_temp = i+1
                while(i_min_temp >= 0 and map[l][i_min_temp][0].isdigit()):
                        s = map[l][i_min_temp][0] + s
                        i_min_temp-=1

                while(i_max_temp <= len(map[0])-1 and map[l][i_max_temp][0].isdigit()):
                        s = s + map[l][i_max_temp][0]
                        i_max_temp += 1
                
                i = i_max_temp
                found.append(s)
            else:
                i+=1
        l+=1
    return found,cont




print(adjacent(lines,1))
print(adjacent(lines,2))