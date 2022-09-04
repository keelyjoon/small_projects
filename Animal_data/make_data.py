from numpy.core.numeric import full
import text_cutter 
import numpy as np
import math

# import data with numpy tools....
animal_names_direct = np.loadtxt('zoo.txt', dtype=str, comments='#', delimiter=None, converters=None, skiprows=1, usecols=0, unpack=False, ndmin=0, encoding='bytes', max_rows=None, like=None)
animal_traits_direct = np.loadtxt('zoo.txt', comments='#', delimiter=None, converters=None, skiprows=1, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=False, ndmin=0, encoding='bytes', max_rows=None, like=None)

"""
get_stuff() method runs the text_cutter file 
to get the data set up to be used in other functions
"""
def get_stuff():
    full_data_set = animal_traits_direct
    first_clusters = text_cutter.clean_data()[1]
    big_set = np.array(full_data_set)
    array_clusters = np.array(first_clusters)
    return [array_clusters, big_set]

"""
calculations() function takes the data of 
array_clusters and big set and does the 
manhattan algorthim
"""
def calculations(data):
    [array_clusters, big_set] = data
    full_data_set = []
    for item in range(7):
        full_data_set.append([])
    # for every animal in the big set of data 
    # loop runs to do the manhattan calculations
    for animal in big_set:
        temp = 1000
        temp_index = 0
        for index, item in enumerate(array_clusters):
            difference = np.subtract(animal, item)
            ab_difference = np.absolute(difference)
            sum_difference = np.sum(ab_difference)
            if sum_difference < temp:
                temp = sum_difference
                temp_index = index
                
        full_data_set[temp_index].append(animal.tolist())
    return full_data_set

"""
euclid_calcuations takes data as an arugment and 
runs the euclid algorithm on the data.
"""
def euclid_calculations(data):
    [array_clusters, big_set] = data
    full_data_set = []
    for item in range(7):
        full_data_set.append([])
    for animal in big_set:
        temp = 1000
        temp_index = 0
        for index, item in enumerate(array_clusters):
            difference = np.subtract(animal, item)
            # square the difference
            square_difference = np.square(difference)
            # sqrt of the sum
            sum_difference = math.sqrt(np.sum(square_difference))
            
            if sum_difference < temp:
                temp = sum_difference
                temp_index = index

        full_data_set[temp_index].append(animal.tolist())
    return full_data_set

"""
new_clusters() function finds the mean of the current
clusters and then returns the new cluster values.
"""
def new_clusters(clusters):
    data_set = clusters
    mean_values = []
    # runs for every item in the data set
    for item in data_set:
        temp = np.mean(item, axis=0)
        new_temp = temp.tolist()
        mean_values.append(new_temp)
    # returns the new cluster mean values
    return mean_values

"""
the compare() function runs with the argument choice_of_method.
runs the calculations method and compares the clusters.
returns the new_set data with help from the calculations function.
"""
def compare(choice_of_method):
    og_list = []
    # conditional to select the method used (manhattan or euclid)
    if choice_of_method == 'manhattan':
        new_set = calculations(get_stuff())
    else:
        new_set = euclid_calculations(get_stuff())
    first_clusters = calculations(get_stuff())
    count = 0
    # while loop runs as long as the og_list does not equal
    # the first clusters. if the clusters are the same, returns
    # that set of data
    while og_list != first_clusters:
        count += 1
        og_list = first_clusters
        list_clusters = new_clusters(first_clusters)
        array_clusters = np.array(list_clusters)
        all_animals = text_cutter.clean_data()[2]
        all_animals_array = np.array(all_animals)
        all_data = [array_clusters, all_animals_array]
        if choice_of_method == 'manhattan':
            new_set = calculations(all_data)
        else:
            new_set = euclid_calculations(all_data)
        first_clusters = calculations(all_data)
    return new_set
"""
final_animal_chart() takes a string as a argument called 
choice_of_method. It calls the compare method with the same 
argument in order to run the main part of the code. Uses other 
file called text_cutter to get the starting clusters. 
"""
def final_animal_chart(choice_of_method):
    animal_clusters = compare(choice_of_method)
    all_animals = text_cutter.clean_data()[2]
    all_animal_names = animal_names_direct
    animal_chart = []
    # for loop goes through the range of 7 (7 different groups).
    # other for loops to append the correct indexes  
    for item in range(7):
        animal_chart.append([])
    for idx, animal in enumerate(all_animals):
        for index, group in enumerate(animal_clusters):
            if animal in group:
                animal_chart[index].append(all_animal_names[idx])
    # conditional that runs the correct algorithm 
    if choice_of_method == 'manhattan':
        print("THE MANHATTAN METHOD:")
    else:
        print("THE EUCLIDIAN METHOD:")
    # prints animal names in correct groups 
    for group in animal_chart:
        print(f"This group had: {len(group)} members.")
        print(f"They were: {group}")
        
final_animal_chart('manhattan')
final_animal_chart('euclid')



