from tkinter import *

# create window
window = Tk()
# set window dimensions
window.geometry("800x500")
window.title("Rock Paper Scissor Game")

# create label
label = Label(window, text="Would you like to play Rock Paper Scissors?", font=("Arial", 22))
label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)


# create entry widget
name_label = Label(window, text="Enter your name", font=("Arial", 18))
name_label.grid_forget()
insert_name = Entry(window)
insert_name.grid_forget()

# create buttons
yes_button = Button(window, text="Yes", font=("Arial", 18), command=lambda: yes_clicked())
no_button = Button(window, text="No", font=("Arial", 18))

yes_button.grid(row=2, column=0, padx=20, pady=20)
no_button.grid(row=2, column=1, padx=20, pady=20)


def yes_clicked():
    insert_name.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
    name_label.grid(row=1, column=0, padx=20, pady=20)
    label.grid_forget()
    yes_button.grid_forget()
    no_button.grid_forget()


window.mainloop()
