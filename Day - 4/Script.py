file = open("input.txt", "r")
content = file.read().split("\n")


WORD = "XMAS"

# content = """
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# """
# content = content[1:-1].split("\n")


# Returns the number of times word is in line
def read_line(line: str, word: str):

    res = 0
    for i in range(len(line) - len(word) + 1):
        if line[i: i + len(word)] == word: res += 1


    return res



result = 0
aux = 0

# All Lines
for line in content:
    line = "".join(line)
    result += read_line(line, WORD)
    result += read_line(line[::-1], WORD)

print(f"Lines: {result}")
aux = result
# All Columns
for j in range(len(content[0])):
    column = [content[i][j] for i in range(len(content))]
    column = "".join(column)

    result += read_line(column, WORD)
    result += read_line(column[::-1], WORD)

print(f"Columns: {result - aux}")
aux = result

diagonal = []

# All Diagonals
# for starting_row in range(len(content) - len(WORD) + 1, -1, -1):
#     row = starting_row
#     diagonal = []

#     for col in range(len(content[0])):
#         if row >= len(content) or row < 0: break
#         diagonal.append(content[row][col])
#         row -= 1

#     diagonal = "".join(diagonal)
    
#     result += read_line(diagonal, WORD)
#     result += read_line(diagonal[::-1], WORD)

#     diagonal = []
#     row = starting_row
#     for col in range(len(content[0]) - 1, - 1, - 1):
#         print(row, col, end=" | ")
#         if row >= len(content) or row < 0: break
#         diagonal.append(content[row][col])
#         row -= 1
    
#     print()
    
#     diagonal = "".join(diagonal)
    
#     result += read_line(diagonal, WORD)
#     result += read_line(diagonal[::-1], WORD)
# matrix = []
# for i in range(5):
#     line = []
#     for j in range(1, 6):
#         line.append(i*5 + j)
#     matrix.append(line)
# print(matrix)
# content = matrix

for starting_row in range(len(content) - len(WORD) + 1):
    row = starting_row
    diagonal = []

    for col in range(len(content[0])):
        if row >= len(content): break
        diagonal.append(content[row][col])
        row += 1

    diagonal = "".join(diagonal)
    
    result += read_line(diagonal, WORD)
    result += read_line(diagonal[::-1], WORD)

    row = starting_row
    diagonal = []

    for col in range(len(content[0]) - 1, -1, -1):
        if row >= len(content): break
        diagonal.append(content[row][col])
        row += 1
    
    diagonal = "".join(diagonal)
    result += read_line(diagonal, WORD)
    result += read_line(diagonal[::-1], WORD)

for starting_col in range(1, len(content[0]) - len(WORD) + 1):
    col = starting_col
    diagonal = []

    for row in range(len(content)):
        if col >= len(content[0]): break
        diagonal.append(content[row][col])
        col += 1
    
    
    diagonal = "".join(diagonal)
    result += read_line(diagonal, WORD)
    result += read_line(diagonal[::-1], WORD)

for starting_col in range(len(content[0]) - len(WORD) + 2, len(WORD) - 2, -1):
    col = starting_col
    diagonal = []

    for row in range(len(content)):
        if col < 0: break
        diagonal.append(content[row][col])
        col -= 1

    diagonal = "".join(diagonal)
    result += read_line(diagonal, WORD)
    result += read_line(diagonal[::-1], WORD)


print(f"Diagonals: {result - aux}")

def x_word(matrix, word):
    res = 0

    print(len(word))
    for i in range(len(matrix) - len(word) + 1):
        for j in range(len(matrix[0]) - len(word) + 1):

            diagonal = "".join([matrix[i + k] [j + k] for k in range(len(word))])
            antidiagonal = "".join([matrix[i + k] [j + len(word) - 1 - k] for k in range(len(word))])
            
            if (word == diagonal or word[::-1] == diagonal) and (word == antidiagonal or word[::-1] == antidiagonal): res += 1

    return res


result = x_word(content, "MAS")
print(f"Answer Part 2: {result}")


