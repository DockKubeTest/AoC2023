def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'AoC\Dec06_Input.txt'
data = read_file(path)

def clean_data(unclean_data):
    cleaned_time = []
    cleaned_distance = []
    new_time_values = ''
    new_distance_values = ''
    for line in unclean_data:
        if "Time" in line:
            remove_heading = line.strip().split('        ')
            time_values = remove_heading[1].strip().split('     ') 
        if "Distance" in line:
            remove_heading = line.strip().split('   ')
            distance_values = remove_heading[1:]
    for time in time_values:
        new_time_values += time
    for distance in distance_values:
        new_distance_values += distance
    return(new_time_values, new_distance_values)

cleaned_data = clean_data(data)
Time_of_race = cleaned_data[0]
Distance_needed = cleaned_data[1]

def race_attempt_winners(race_results, distance_needed_to_win): 
    counter = 0
    for num in race_results:
        if num > int(distance_needed_to_win):
            counter += 1
    return(counter)


def race_options(total_time, distance_needed_to_win):
    result_possibilities = []
    distance_values = []
    race_time = int(total_time)
    attempt_range = range(race_time)
    for attempt in attempt_range:
        speed = int(attempt)
        time_held = int(attempt)
        distance_travelled = speed * (race_time - time_held)
        distance_values.append(distance_travelled)
        #print(f'For race {race}, we hold for {time_held}ms, the boat goes {speed} per ms and travels {distance_travelled}mm.')
    count_of_winners = race_attempt_winners(distance_values, distance_needed_to_win)
    result_possibilities.append(race_attempt_winners(distance_values, distance_needed_to_win))
    return(result_possibilities)

results = race_options(Time_of_race, Distance_needed)

def multiplier(mylist):
    result = 1
    for x in mylist:
        result = result * x
    return(result)

print(multiplier(results))

# Formula:
# distance travelled = speed*(total time - time held)