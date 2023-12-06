import re 

file = open("input")
lines = [ line.strip('\n') for line in file ]
file.close()

card_counts: list[int] = [ 1 for _ in range(len(lines))]

sum = 0
for i in range(len(lines)):
    count = 0

    numbers = [
        match.group(0) 
        for match in re.finditer(r"([0-9]|[ ])++", lines[i])
    ]
    winning_numbers: list[int] = [
        int(match.group(0))
        for match in re.finditer(r"([0-9])++", numbers[1])
    ]
    card_numbers: list[int] = [
        int(match.group(0))
        for match in re.finditer(r"([0-9])++", numbers[2])
    ]

    matches: int = 0
    for num in card_numbers:
        if num in winning_numbers:
            matches += 1

    # part 1
    # if matches > 0:
    #     sum += pow(2, matches - 1);
    
    # basically, for every card ahead, add the number of duplicates of the current card
    for x in range(matches):
        card_counts[1 + i + x] += card_counts[i] 

    # then get the sum
    sum += card_counts[i]

print(sum) 