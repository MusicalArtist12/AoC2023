import re 

def convertnum(x: str):
    match x:
        case "one": return 1
        case "two": return 2
        case "three": return 3
        case "four": return 4
        case "five": return 5
        case "six": return 6
        case "seven": return 7
        case "eight": return 8
        case "nine": return 9
        case _: return int(x)

file = open("input")
sum = 0;
for line in file:
    line = line.strip('\n')
    matches = re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))', line)
    results: list[str] = [str(match.group(1)) for match in matches]
    final: list[int] = [convertnum(i) for i in results]
    num: int = final[0] * 10 + final[final.__len__()-1];
    sum += num
    print(f"{num} = {final} {line}")

file.close()
print(sum)
