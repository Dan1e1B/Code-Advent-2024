# Part 1
file = open("input.txt", "r")
content = file.read().split("\n")


result = 0

for line in content:
    lst = [int(num) for num in line.split(" ")]

    safe = True
    ascending = 0
    decreasing = 0

    for i in range(len(lst) - 1):
        if lst[i] < lst[i+1] < lst[i] + 4: ascending += 1
        elif lst[i] - 4 < lst[i+1] < lst[i]: decreasing += 1
        else: safe = False; break

        # Part One
        # if ascending > 0 and decreasing > 0: safe = False; break
        if ascending > 1 and decreasing > 1: safe = False; break
    
    if safe: result += 1

print(f"Answer Part One: {result}")

# Part 2




