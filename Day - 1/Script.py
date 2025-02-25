# Star 1
file = open("Input - First Star.txt", "r")
content = file.read().split("\n")

# print(content)
list1 = []
list2 = []

for line in content:
    lst = line.split("  ")

    list1.append(int (lst[0]))
    list2.append(int (lst[1]))

result = 0

list1.sort()
list2.sort()

for i in range(len(content)):
    result += max(list1[i], list2[i]) - min(list1[i], list2[i])

# Final Answer Star One
print(f"Answer: {result}")

# Star 2
dict2 = {}

for num in list2:
    if dict2.get(num): dict2[num] += 1
    else: dict2[num] = 1

result = 0

for num in list1:
    if dict2.get(num): result += num * dict2[num]

# Answer Star 2
print(f'Answer Star 2: {result}')