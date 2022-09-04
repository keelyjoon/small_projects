from tkinter.filedialog import askdirectory
import pathlib
import glob

# this function uses askdirectory to find
# the directory where txt files are
def directory_picker():
    data_directory = askdirectory(initialdir = str(pathlib.Path().resolve()) + "/Documents_1/")
    print(data_directory)
    return data_directory

# this function uses the function
# directory_picker and returns
# the text_files 
def file_picker():
    folder = directory_picker()
    text_files = glob.glob(folder + "/" + "*.txt")

    return text_files