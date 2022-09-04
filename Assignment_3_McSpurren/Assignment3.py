# Name:   <Keelyjoon McSpurren>
# Student Number: <20272478>
# Email:  <20kjmm@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

from gui import file_picker

# this function takes a list and checks to see 
# if the word is a valid word. It also checks to
# see if the word is greater than or equal to 5 chars.
# then returns the list of clean/valid words
def good_list(list):
    clean_words = []
    for word in list:
        clean_word = ''
        for letter in word:
            if letter.isalpha() or letter == "'":
                clean_word += letter        
        if len(clean_word) >= 5:
            clean_words.append(clean_word)
    return(clean_words)

# this function opens the StopWords.txt and 
#creates a list containing all the words 
# this list will then be checked against the 
# lists containing the words in the chosen txt
#files. Returns the list of stop words
def stop_words():
    stop_words = open("StopWords.txt", "r")
    bad_words = []
    bad_words = stop_words.read().split()
    return(bad_words)

# this function takes a list and checks to see 
# if any of the stop words are in the list.
# if a word from the list is not in the stop words list,
# then it adds that word to a new list.
# Returns the new list
def check_lists(list):
    bad = stop_words()
    good_list = []
    for word in list:
        if word not in bad:
            good_list.append(word)
    return(good_list)

# this function takes two txt files, opens them, and runs a number 
# of functions to then return two lists that are valid and ready
# to be minipulated 
def two_files(file1, file2):
    #opens file one and makes into list
    file1_open = open(file1, "r")
    words1 = []
    words1 = file1_open.read().split()
    # takes words1 and checks against stop words list
    no_stop_words1 = check_lists(words1)
    # takes no_stop_words1 and checks to make sure words are valid
    valid_words_1 = good_list(no_stop_words1)

    #opens file two and makes into list
    file2_open = open(file2, "r")
    words2 = []
    words2 = file2_open.read().split()
    # takes words2 and checks against stop words list
    no_stop_words2 = check_lists(words2)
    # takes no_stop_words2 and checks to make sure words are valid
    valid_words_2 = good_list(no_stop_words2)

    #returns 2 vaild lists ready to be made into dicts
    return[valid_words_1, valid_words_2]

# this function makes dicts out of lists.
# it takes 2 arguments which will be the chosen txt files.
# it calls the two_files function and returns two dicts
def make_dict(book1, book2):
    split = two_files(book1, book2)

    #book1 becomes lst1
    lst1 = split[0]
    # makes dict with lst1
    word_counter1 = {}
    for word in lst1:
        if word in word_counter1.keys():
            word_counter1[word] += 1
        elif word not in word_counter1.keys():
            word_counter1[word] = 1

    #book2 becomes lst2
    lst2 = split[1]
    word_counter2 = {}  
    # makes dict with lst2
    for word in lst2:
        if word in word_counter2.keys():
            word_counter2[word] += 1
        elif word not in word_counter2.keys():
            word_counter2[word] = 1

    return[word_counter1, word_counter2]

# this function kills off unwanted keys/values 
# using the dicts from make_dict() it then 
# returns two dicts
# it takes 2 arguments which will be the chosen txt files
def kill_off(book1, book2):
    # splits the return value of make_dict() into two dicts
    split = make_dict(book1, book2)
    dict_first = split[0]
    dict_second = split[1]

    # deletes values/key from dict if the word is repeated
    # less than 5 times in the dict.
    # does this for both dicts
    delete1 = []
    ready_to_kill_dict1 = dict_first
    for key, val in ready_to_kill_dict1.items():
        if val < 5:
            delete1.append(key)
    for i in delete1:
        del ready_to_kill_dict1[i]

    delete2 = []
    ready_to_kill_dict2 = dict_second
    for key, val in ready_to_kill_dict2.items():
        if val < 5:
            delete2.append(key)
    for i in delete2:
        del ready_to_kill_dict2[i]
    return(ready_to_kill_dict1, ready_to_kill_dict2)

# this function takes the dicts from the 
# function kill_off() and turns them back 
# into lists so that they can be calculated later
# it returns two lists
# it takes 2 arguments which will be the chosen txt files
def dict_to_list(book1, book2):
    split = kill_off(book1, book2)
    dict_first = split[0]
    dict_second = split[1]
    list1 = list(dict_first.keys())
    list2 = list(dict_second.keys())
    print("First set:", list1, "\n \n Second set:", list2)

    return[list1,list2]

# this function does the jaccard similarity 
# calculation of the two lists 
# it takes 2 arguments which will be the chosen txt files
def calculation(book1, book2):
    # splits the return value of dict_to_list() 
    # creating two lists ready to be calculated
    split = dict_to_list(book1, book2)
    lst1 = split[0]
    lst2 = split[1]
    # creates a list for the intersecting values of the two lists
    lst3 = [value for value in lst1 if value in lst2]
    # finds the length of the intersecting values list
    intersection = len(lst3)
    # finds the union of the two lists
    final_list = list(set(lst1) | set(lst2))
    print("The intersection between the words in the two text files was:", intersection, "words")
    union = len(final_list)
    print("The union between the words in the two text files was:", union, "words")
    jaccard_similarity = str(round(intersection / union, 3))
    print("The jaccard similarity of the words in the two text files is:"+ jaccard_similarity)
    return "The jaccard similarity of the words in the two text files is:"+ jaccard_similarity
