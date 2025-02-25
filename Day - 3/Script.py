file = open("input.txt", "r")
content = file.read()

CORRECT_STRNG = "mul("
numbers = 0
index = 0
is_strng = False
is_inputing_number = False

lst = []


for letter in content:

    if letter is "m": is_strng = True; index = 1
    elif is_strng:
        
        if (0 < index < 4) and (CORRECT_STRNG[index] != letter): 
            is_strng = False
            index = 0
            continue

        elif (index == 4) or (index == 5):
            if (letter is ",") and (is_inputing_number == True):
                is_inputing_number = False
                
        index += 1
        
