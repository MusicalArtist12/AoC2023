import re 

file = open("input")
lines = [ line.strip('\n') for line in file ]
file.close()

linenums: list[list[tuple[str, int]]] = []
linestars: list[list[int]] = []

for line in lines:

    # 0 = value, 1 = start pos
    nums = [
        ( str(match.group(1)), match.start() ) 
        for match in re.finditer(r'([0-9]++)', line)
    ]

    stars = [
        match.start()
        for match in re.finditer(r'([*])', line)
    ]

    linenums.append(nums)
    linestars.append(stars)


sum = 0
idx = 0
while idx < len(linenums):
    top_nums = [] if (idx - 1) < 0 else linenums[idx - 1]
    mid_nums = linenums[idx]
    bot_nums = [] if (idx + 1) >= len(linenums) else linenums[idx + 1]

    nums = top_nums + mid_nums + bot_nums
    stars = linestars[idx]

    for star in stars:
        attached_nums: list[int] = []

        for num in nums:
            start = num[1] - 1
            end = num[1] + len(num[0])

            if start <= star and star <= end:
                attached_nums.append(int(num[0]))

        if len(attached_nums) == 2:
            ratio = attached_nums[0] * attached_nums[1]
            sum += ratio

    idx += 1

print(sum)