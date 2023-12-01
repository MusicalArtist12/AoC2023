# each line has a number overlapping with characters
# remove the characters and only use numbers
# get the sum of the numbers

import re 

file = open("input",)

sum = 0;
for line in file:
    line = line.strip('\n')
    
    m = re.sub("[A-Za-z]", "", line)

    fin = m[0] + m[m.__len__()-1];

    print(f"{sum} += {fin} <- {m} <- {line}")
    sum += int(fin);

file.close()

print(sum)
