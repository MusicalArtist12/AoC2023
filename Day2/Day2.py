# Julia Abdel-Monem (juliaviolet.dev)
# Advent of Code 2023
# Day 2

import re 

file = open("input")
sum = 0;
for line in file:
    line = line.strip('\n')
    linenum = re.match(r'(Game)( )([0-9]++)', line)
    if linenum == None:
        raise Exception("line number does not exist")

    num = int(re.sub("Game ", "", linenum.group()))

    reds = re.finditer(r'([0-9]++)( )(red)', line)
    redset: list[int] = [int(match.group(1)) for match in reds]

    greens = re.finditer(r'([0-9]++)( )(green)', line)
    greenset: list[int] = [int(match.group(1)) for match in greens]

    blues = re.finditer(r'([0-9]++)( )(blue)', line)
    blueset: list[int] = [int(match.group(1)) for match in blues]
    
    # print(redset)
    # print(greenset)
    # print(blueset)

    # Part 1
#   valid: bool = True
#   MAX_RED = 12
#   MAX_GREEN = 13
#   MAX_BLUE = 14
#
#   for red in redset:
#       if red > MAX_RED:
#           valid = False
#           break
#   
#   for green in greenset:
#       if green > MAX_GREEN:
#           valid = False
#           break
#
#   for blue in blueset:
#       if blue > MAX_BLUE:
#           valid = False
#           break
#   
#   print(f"{num} is {valid}")
#
#   if valid: 
#       sum += num

    # Part 2
    highestred = 0
    for red in redset:
        if red > highestred:
            highestred = red

    highestgreen = 0
    for green in greenset:
        if green > highestgreen:
            highestgreen = green

    highestblue = 0
    for blue in blueset:
        if blue > highestblue:
            highestblue = blue

    setpow = highestred * highestgreen * highestblue
    sum += setpow

    # print(f"{num} has a power of {setpow}")

file.close()
print(f"the sum is: {sum}")
