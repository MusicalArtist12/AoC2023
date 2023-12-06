import re 

file = open("test")
lines = [ line.strip('\n') for line in file ]
file.close()

for line in lines:
    numbers = re.finditer(r"([0-9]++|\|)", line)
    numbers = [match.group(0) for match in numbers]

    winning_numbers: list[int] = []
    for number in numbers:
        if number == '|':
            break
            
        winning_numbers.append(int(number))
        

    print(winning_numbers)