file = open("input.txt", "r")
content = file.read().split("\n")


result = 0




def is_safe(lst):
    safe = True
    ascending = lst[0] < lst[1]
    for i in range(len(lst) - 1):

      #  if switched_increment:
            
       #     switched_increment = False
        #    continue
        if ascending and not(lst[i] < lst[i+1] < lst[i] + 4): 
            safe = False; break

        elif not ascending and not (lst[i] - 4 < lst[i+1] < lst[i]): 
            safe = False; break
        
        
    
        # else: safe = False; break

        # Part One
        # if ascending > 0 and decreasing > 0: safe = False; break
        # if ascending > 1 and decreasing > 1: safe = False; break
    
    return safe

# Part 1
for line in content:
    lst = [int(num) for num in line.split(" ")]

    if is_safe(lst): result += 1

print(f"Answer Part One: {result}")
result = 0

# Part 2
for line in content:
    lst = [int(num) for num in line.split(" ")]

    for i in range(len(lst)):
        aux = lst.copy()
        aux.pop(i)
        if (is_safe(aux)):  result += 1; break



print(f"Answer Part Two: {result}")

# Part 2




