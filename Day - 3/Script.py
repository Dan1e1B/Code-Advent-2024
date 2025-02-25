file = open("input.txt", "r")
content = file.read()

CORRECT_STRNG = "mul("
INSTRUCTION_DO = "do("
INSTRUCTION_DONT = "don't("

enabled_mul = True
index_mul = 0
reading_mul = False
is_reading_number = False

reading_instruction = False
instruction = INSTRUCTION_DO
index_instruction = 0


lst = []

number1 = 0
number2 = 0

# content = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

for letter in content:

    # Part 2 --> Comment for Part 1 Answer <--
    if letter == "d":
        reading_instruction = True
        index_instruction = 1
        reading_mul = False
    
    elif reading_instruction:
        if ((index_instruction == 1) and (letter == "o")) or (2 < index_instruction < len(instruction) and (instruction[index_instruction] == letter)): pass
        elif (index_instruction == 2) and (letter in ("n", "(")): instruction = INSTRUCTION_DO if letter == "(" else INSTRUCTION_DONT
        
        elif (index_instruction == len(instruction)) and (letter == ")"):
            enabled_mul = instruction == INSTRUCTION_DO
            reading_instruction = False

        else: reading_instruction = False; print(letter, index_instruction, instruction)
        index_instruction += 1
    # End of Part 2

    # Part 1
    if enabled_mul and letter == "m": 
        reading_mul = True
        index = 1
        is_reading_number = False
        number1 = 0
        number2 = 0
        

    elif reading_mul:
        
        if (0 < index < 4) and (CORRECT_STRNG[index] != letter): reading_mul = False
            
        elif (0 < index < 4): index += 1

        elif (index == 4) or (index == 5):
            if (letter == ",") and (index == 4):

                if not (is_reading_number == True): reading_mul = False
                
                is_reading_number = False
                index += 1

            elif (letter.isdigit()):

                is_reading_number = True

                if (index == 4): number1 = number1 * 10 + (int)(letter)
                elif (index == 5): number2 = number2 * 10 + (int)(letter)

                if number1 >= 1000 or number2 >= 1000: reading_mul = False
            
            elif (letter == ")"):
                reading_mul = False
                lst.append((number1, number2))
            
            else: reading_mul = False


result = 0            
for (x, y) in lst:
    result += x * y

print(f"Answer: {result}")
        
