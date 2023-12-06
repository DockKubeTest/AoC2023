def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'AoC/Dec03_Input.txt'
data = read_file(path)
special_chars = ['@', '#', '$', '%', '/', '*', '+', '=', '&', '-']
product_list = []

def right_horizontal_check(symbol_location, line_schematics):
    clean_line = line_schematics.strip()
    line_length = len(clean_line)
    iterator = symbol_location + 1
    num = ''
    while iterator < line_length:
        if line_schematics[iterator].isdigit():
            num += line_schematics[iterator]
        else:
            break
        iterator += 1
    return(num)

def left_horizontal_check(symbol_location, line_schematics):
    clean_line = line_schematics.strip()
    line_length = len(clean_line)
    iterator = symbol_location - 1
    num = ''
    while iterator >= 0:
        if line_schematics[iterator].isdigit():
            num = line_schematics[iterator] + num
        else:
            break
        iterator -= 1
    return(num)

def lower_horizontal_check(symbol_index, lower_line_schematics):
    global product_list
    clean_line = lower_line_schematics.strip()
    line_length = len(clean_line)
    num = lower_line_schematics[symbol_index] if lower_line_schematics[symbol_index].isdigit() else ''
    num1 = ''
    num2 = ''
    iterator = symbol_index - 1
    while iterator >= 0:
        if lower_line_schematics[iterator].isdigit():
            if num == '':
                num2 = lower_line_schematics[iterator] + num2
            else:
                num = lower_line_schematics[iterator] + num
        else:
            break
        iterator -= 1
    
    iterator = symbol_index + 1
    while iterator < line_length:
        if lower_line_schematics[iterator].isdigit():
            if num == '':
                num1 += lower_line_schematics[iterator]
            else:
                num += lower_line_schematics[iterator]
        else:
            break
        iterator += 1

    if num1.isdigit():
        product_list.append(int(num1))
    if num2.isdigit():
        product_list.append(int(num2))
    if num.isdigit():
        product_list.append(int(num))
    print(num)
    print(num1)
    print(num2)
    return()

def upper_horizontal_check(symbol_index, upper_line_schematics):
    global product_list
    clean_line = upper_line_schematics.strip()
    line_length = len(clean_line)
    num = upper_line_schematics[symbol_index] if upper_line_schematics[symbol_index].isdigit() else ''
    num1 = ''
    num2 = ''
    iterator = symbol_index - 1
    while iterator >= 0:
        if upper_line_schematics[iterator].isdigit():
            if num == '':
                num2 = upper_line_schematics[iterator] + num2
            else:
                num = upper_line_schematics[iterator] + num
        else:
            break
        iterator -= 1

    iterator = symbol_index + 1
    while iterator < line_length:
        if upper_line_schematics[iterator].isdigit():
            if num == '':
                num1 += upper_line_schematics[iterator]
            else:
                num += upper_line_schematics[iterator]
        else:
            break
        iterator += 1

    if num1.isdigit():
        product_list.append(int(num1))
    if num2.isdigit():
        product_list.append(int(num2))
    if num.isdigit():
        product_list.append(int(num))
    print(num)
    print(num1)
    print(num2)
    return()

def find_special_char(engine_schematics):
    global product_list
    counter = 0
    for line_number, line in enumerate(engine_schematics):
        for char_number, char in enumerate(line):
            if char in special_chars:
                right_check = right_horizontal_check(char_number, line)
                left_check = left_horizontal_check(char_number, line)
                if right_check.isdigit():
                    product_list.append(int(right_check))
                if left_check.isdigit():
                    product_list.append(int(left_check))
                if (line_number + 1) <= (len(engine_schematics) - 1):
                    lower_horizontal_check(char_number, engine_schematics[line_number + 1])
                if (line_number - 1) >= 0:
                    upper_horizontal_check(char_number, engine_schematics[line_number - 1])


find_special_char(data)
print(product_list)
print(len(product_list))
sum_of_product = sum(product_list)
print(sum_of_product)
