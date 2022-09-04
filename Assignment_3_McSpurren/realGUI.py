from tkinter import *
from tkinter import ttk
from gui import file_picker
from Assignment3 import calculation

# creates the base for the GUI
root = Tk()
root.title("Book Reco")

# basic sizing and padding for main display
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, columnspan=2, rowspan=5, sticky=(N, W, E, S))

# will hold and display the value of the Jaccard result
result = StringVar()

# creates a list of all the books in the available directory calling book_list(
available_books = file_picker()
# variables for the two choices the user makes
choice1 = StringVar()
choice2 = StringVar()

choices = available_books
pick1_button = ttk.Label(mainframe, text="First Book Choice")
pick1_button.grid(column=0, row=1)

# show the list of books
row = 2
for item in choices:
    thing = ttk.Radiobutton(mainframe, text=item, variable=choice1, value=item)
    thing.grid(column=0, row=row)
    row += 1

# once the user makes two choices and hits the button, execute this and 
# run the main program to parse out unwanted words and return the calculation
def print_pick(*args):
    print(str(choice1.get()))
    print(str(choice2.get()))
    result.set(calculation(str(choice1.get()), str(choice2.get())))

choices2 = available_books
pick2_button = ttk.Label(mainframe, text="Second Choice")
pick2_button.grid(column=1, row=1)

row = 2
for item in choices2:
    thing = ttk.Radiobutton(mainframe, text=item, variable=choice2, value=item)
    thing.grid(column=1, row=row)
    row += 1

# format the pick button and place the result in center of screen
pick_me = ttk.Button(mainframe, text='Pick your two books', command=print_pick)
pick_me.grid(columnspan=2)
main_result = ttk.Label(mainframe, textvariable=result)
main_result.grid(columnspan=2)

# allow the user to cancel and close the dialog box
end = ttk.Button(root, text="Quit", command=root.destroy)
end.grid(columnspan=2)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

def gui_runs():
    root.mainloop()

gui_runs()