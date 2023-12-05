# ideas: load three rows at a time, then increment row by row, overwriting the previous one
# probably best to treat it as a 2d array, index
import re 

file = open("input")

lines = [ line.strip('\n') for line in file ]
file.close()

linenums: list[list[tuple[str, int]]] = []
linesymbols: list[list[int]] = []

for line in lines:

    # 0 = value, 1 = start pos
    nums = [
        ( str(match.group(1)), match.start() ) 
        for match in re.finditer(r'([0-9]++)', line)
    ]

    symbols = [
        match.start()
        for match in re.finditer(r'([!|@|#|$|%|^|&|*|\-|+|\/|=])', line)
    ]

    linenums.append(nums)
    linesymbols.append(symbols)

sum = 0
idx = 0
while idx < len(linenums):
    nums = linenums[idx]

    top_symbols = [] if (idx - 1) < 0 else linesymbols[idx - 1]
    mid_symbols = linesymbols[idx]
    bot_symbols = [] if (idx + 1) >= len(linenums) else linesymbols[idx + 1]

    symbols = top_symbols + mid_symbols + bot_symbols

    for num in nums:
        start = num[1] - 1
        end = num[1] + len(num[0])

        #print(f"checking {num}: {start}, {end}")
        #print(f"symbols: top: {top_symbols}, mid: {mid_symbols}, bottom: {bot_symbols}")

        for sym in symbols:
            if start <= sym and sym <= end:
                #print(f"adding {num[0]}")
                sum += int(num[0])
                break

    idx += 1


print(sum)