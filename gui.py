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
no_button = Button(window, text="No", font=("Arial", 18), command=lambda: window.destroy())

# game buttons
rock_button = Button(window, text="Rock", font=("Arial", 18))
paper_button = Button(window, text="Paper", font=("Arial", 18))
scissor_button = Button(window, text="Scissor", font=("Arial", 18))

yes_button.grid(row=2, column=0, padx=20, pady=20)
no_button.grid(row=2, column=1, padx=20, pady=20)

# global variable to store player name
player_name = ""


def yes_clicked():
    global player_name
    insert_name.grid(row=3, column=0, padx=20, pady=20)
    insert_name.bind('<Return>', lambda event: get_player())
    name_label.grid(row=1, column=0, padx=20, pady=20)
    label.grid_forget()
    yes_button.grid_forget()
    no_button.grid_forget()
    insert_name.focus()


def get_player():
    global player_name
    player_name = insert_name.get()
    player_score_label = Label(window, text=f'{player_name}: 0')
    player_score_label.grid(row=0, column=100)
    computer_score_label = Label(window, text='Computer: 0')
    computer_score_label.grid(row=1, column=100)
    name_label.grid_forget()
    insert_name.grid_forget()
    rock_button.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
    paper_button.grid(row=4, column=3, padx=20, pady=20, columnspan=2)
    scissor_button.grid(row=4, column=6, padx=20, pady=20, columnspan=2)


window.mainloop()
