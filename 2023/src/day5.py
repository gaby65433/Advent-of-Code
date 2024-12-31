text = open('../inputs/day5.txt','r').read()

def part1_opt(text):
    mapa = {}
    blocks = text.split("\n\n")
    seeds = list(map(lambda x: int(x),blocks[0].split(':')[1].strip().split(' ')))
    for seed in seeds:
        mapa[seed] = seed
    for block in blocks[1:]:
        block = block.split('\n')[1:]
        done = {}
        for seed in seeds:
            done[seed] = False
        for info in block:
            info = info.split(' ')
            dest,source,rang = int(info[0]),int(info[1]),int(info[2])
            for seed,value in mapa.items():
                #print("range->",source,source+rang)
                if (value in range(source,source + rang) and not(done[seed])):
                    mapa[seed] = dest + value - source
                    done[seed] = True

    return min(mapa.values())

def part2_opt(text):
    answer = []
    blocks = text.split("\n\n")
    seeds = list(map(lambda x: int(x),blocks[0].split(':')[1].strip().split(' ')))
    for i in range(0,len(seeds),2):
        start_seed,seed_range,jump = seeds[i],seeds[i+1],seeds[i+1]
        actualseed = start_seed
        while actualseed <= start_seed + seed_range:
            val = actualseed
            for block in blocks[1:]:
                block = block.split('\n')[1:]
                for info in block:
                    info = info.split(' ')
                    dest,source,rang = int(info[0]),int(info[1]),int(info[2])
                    if source <= val and val < source + rang:
                        jump = min(jump, source + rang - val) #Salta todos ou salta todos so valores que estão no intervalo menores ao val
                        val = dest + val - source
                        if jump <= 0:
                            jump = 1
                        break

            
            actualseed += jump
            #if jump != 1:
            #    print(f"Saltei {jump} seus caralhos")
            jump = seed_range - actualseed + start_seed ## Salta todos os que ainda faltam
            answer.append(val)

    return min(answer)

print(part1_opt(text))
print(part2_opt(text))