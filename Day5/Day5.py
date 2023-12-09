import re 

# lines[0] always corresponds to the list of input seeds

def getMaps(lines: list[str]):
    start = 0
    idx = 0
    maps: list[list[str]] = []

    for line in lines:
        if "map" in line:
            maps.append(lines[start:idx-1])
            #print(f"{start}, {idx}")
            #print(lines[start:idx])

            start = idx
        idx += 1

    # take care of last map, since it does not end with the start of another map
    maps.append(lines[start:idx])
    #print(lines[start:idx])

    return maps

# part 1
#def getSeeds(map: list[str]):
#    seeds: list[int] = []
#    if "seeds:" in map[0]:
#        seeds = [
#            int(match.group(0))
#            for match in re.finditer(r"([0-9])++", map[0])
#        ]
#
#    return seeds 

def getSeeds(map: list[str]):
    seedSets: list[tuple[int, int]] = []
        
    if "seeds:" in map[0]:
        seeds = [
            int(match.group(0))
            for match in re.finditer(r"([0-9])++", map[0])
        ]


        i = 0
        while i < len(seeds):
            seedSets.append((seeds[i], seeds[i] + (seeds[i + 1] - 1)) )
            i += 2

    return seedSets

def processMaps(maps: list[list[str]]):
    processedMaps: dict[str, list[tuple[int, int, int]]] = {}

    for map in maps:

        myMap: list[tuple[int, int, int]] = []

        for line in map[1:]:
            nums = [
                int(match.group(0))
                for match in re.finditer(r"([0-9])++", line)
            ]

            destStart = nums[0]
            sourceStart = nums[1]
            numRange = nums[2]

            myMap.append((destStart, sourceStart, numRange))

            # print(f"{sourceStart} -> {destStart}; {numRange}")        
        name = re.sub(r"( map:)", "", map[0]);
        processedMaps[name] = myMap

    return processedMaps

# returns the tuple in a list of size 1 if it maps completely, and more than 1 if it does not. will be in order where (lowest, highest) -> [(lowest, a), (b, c), (d, highest)]
# returns the input tuple in the list if it does not map at all
def mapSeed(seed: tuple[int, int], domain: tuple[int, int], offset: int) -> list[tuple[int, int]]:
    mySets: list[tuple[int, int]] = []
 
    while seed != (0, 0):
        #print(f"checking {seed}")
        if seed[0] < domain[0]:
            if seed[1] < domain[0]:
                mySets.append(seed)
                seed = (0, 0)

            elif seed[1] >= domain[0]:
                mySets.append((seed[0], domain[0] - 1))
                seed = (domain[0], seed[1])

        elif seed[0] >= domain[0] and seed[0] < domain[1]:
            if seed[1] <= domain[1]:
                mySets = [(seed[0] + offset, seed[1] + offset)] + mySets
                seed = (0, 0)
            
            elif seed[1] > domain[1]:
                mySets = [(seed[0] + offset, domain[1] + offset)] + mySets
                seed = (domain[1] + 1, seed[1])
        
        elif seed[0] > domain[1]:
            mySets.append(seed)
            seed = (0, 0)

        #print(mySets)
    #print()
    return mySets

file = open("input")
lines = [ line.strip('\n') for line in file ]
file.close()

maps = getMaps(lines)
seeds = getSeeds(maps[0])
maps = processMaps(maps[1:])

# part 1
#for i in range(len(seeds)):
#    print(seeds[i])
#    
#    for name in maps:
#        print(name)
#        current = seeds[i]
#        new = current
#
#        for map in maps[name]:
#            # print(map)
#            if map[1] <= current and current < (map[1] + map[2]):
#                new = (current - map[1]) + (map[0])
#
#                break
#
#        print(f"{current} -> {new}")
#        # print()
#        seeds[i] = new
#    print()
#
#seeds.sort()
#print(seeds[0])

for key in maps:
    newseeds = []

    for seed in seeds:
        #print(seeds)
        # cases: does not fit at all, fits completely, only upper range, only lower range 
        newseed = seed 

        for map in maps.get(key):
            in_domain = (map[1], map[1] + (map[2] - 1))
            offset = map[0] - map[1]

            #print(f"seed: {seed} in: {in_domain}, offset: {offset}")
            output = mapSeed(seed, in_domain, offset)
            #print(f"output: {output}") 
            
            if len(output[1:]) > 0:
                seeds += output[1:]       
    
            if newseed == seed and output[0] != seed:
                newseed = output[0]
                break

        newseeds.append(newseed)

    #print(f"newseeds: {newseeds}")
    seeds = newseeds

finalSet = [seed[0] for seed in seeds]

finalSet.sort()

print(finalSet[0])