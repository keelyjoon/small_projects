import random as ran

# open the text file and break it into lists


# RUN MAKE_DATA 
a_file = open("zoo.txt", "r")

data_set = []
for line in a_file:
  line_list = line.split()
  data_set.append(line_list)
a_file.close()

# modify the lists into characteristics, animal names and the data to be analyzed
animal_names = []
characteristics = data_set.pop(0)
for item in data_set:
    animal_names.append(item.pop(0))

# all the info is in different lists now...
data_set = [list( map(int,i) ) for i in data_set]

# this function makes sure our 7 clusters have NO repeats...
# meaning an animal with exactly the same characteristics 
# this could easily lead to clusters with nothing on iterations
def clean_data():
    picker = []
    indexes_we_need = []
    while len(picker) < 7:
        newnum = ran.randint(0, len(animal_names) - 1)
        item = data_set[newnum]
        if item not in picker:
            picker.append(item)
            indexes_we_need.append(newnum)
    picker = [list( map(int,i) ) for i in picker]
    indexes_we_need = [int(i) for i in indexes_we_need]

    return [indexes_we_need, picker, data_set]