def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'Dec04_Input.txt'
data = read_file(path)
running_total = int(0)

def clean_data(unclean_data):
    temp_list = []
    split_game = unclean_data.strip().split(':')
    separate_values = split_game[-1].strip().split('|')
    further_clean(separate_values)
    return()

def further_clean(cleaned_line):
    value = cleaned_line[0].strip().split(' ')
    check = cleaned_line[-1].strip().split(' ')
    compare_lists(value, check)
    return()

def compare_lists(value, check):
    counter = 0
    for val in value:
        if val in check and val != '':
            counter += 1
    if counter > 0:
        add_to_global_var(counter)
    return()

def add_to_global_var(current_count):
    global running_total
    if current_count == 1:
        new_count = 1
    else:
        new_count = int(2**(current_count - 1))
    running_total += new_count
    return()

def line_by_line(full_data):
    for line in full_data:
        clean_data(line)
    return()

cleaned_data = line_by_line(data)
print(running_total)