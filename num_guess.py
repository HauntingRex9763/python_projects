# Number Guessing Game, by Jackson Urquhart - 2022, 2, 28 12:11

import random as rand, tkinter as tk

def create_initial_entries():
    def min_collect_func(args = None): # Func to place curser in min_num
        min_num = int(min_number_entry.get()); min_number_entry.grid_remove() # Get and remove min num entry
        min_num_label.grid_remove()# Remove min num label

        max_number_entry = tk.Entry( # Max num entry, label and focus
            window,  
            background = bg, 
            width = 5,  
            border = 1, 
            cursor = 'dot',  
            foreground = fg,  
        ); max_number_entry.grid( 
            row=1, 
            column=1
        ); max_num_label = tk.Label(  
        text = 'Enter max number here, press enter when done' 
        ); max_num_label.grid( 
            row = 1,
            column=2
        ); max_number_entry.focus() 

        window.bind('<Return>', lambda event: max_collect_func(min_num, max_number_entry, max_num_label)) # Bind enter to entry move func
    
    def max_collect_func(min_num, max_number_entry, max_num_label): # Func to place curser to max_num
        max_num = int(max_number_entry.get()); max_number_entry.grid_remove() # Get and remove max num entry
        max_num_label.grid_remove() # Remove max num label

        max_guesses = int(round((max_num - min_num) * 0.1, 0))
        if max_guesses < 3: max_guesses = 3
        current_guesses = 0
        num_to_guess = rand.randint(min_num, max_num)
        print(num_to_guess)
        status = 'Type a number and press enter to begin guessing!'
        create_guess_entry(num_to_guess, max_guesses, current_guesses, status)
    
    if __name__ == '__main__':
        min_number_entry = tk.Entry( # Min num entry, label and focus
            window, 
            background = bg, 
            width = 5, 
            border = 1,
            cursor = 'dot', 
            foreground = fg,
        ); min_number_entry.grid(
            row=1, 
            column=1
        ); min_num_label = tk.Label( 
        text = 'Enter min number here, press enter when done' 
        ); min_num_label.grid( 
            row = 1,
            column=2
        ); min_number_entry.focus()

        window.bind('<Return>', min_collect_func) # Bind enter to max_num_func

def create_guess_entry(num_to_guess, max_guesses, current_guesses, status):
    label = tk.Label( # Create guess entry, label, and focus
        text = status
    ); label.grid(
        column = 2,
        row = 1
    ); guess_entry = tk.Entry( 
        window, 
        background = bg, 
        width = 5, 
        border = 1, 
        cursor = 'dot', 
        foreground = fg,
    ); guess_entry.grid( 
        row=1, 
        column=1
    ); guess_entry.focus()
    
    window.bind('<Return>', lambda event: get_guess_entry(guess_entry, num_to_guess, max_guesses, current_guesses, label)) # Bind enter to entry get func

def get_guess_entry(guess_entry, num_to_guess, max_guesses, current_guesses, label):
    guess = int(guess_entry.get())
    guess_entry.grid_remove()
    label.grid_remove()
    if (num_to_guess - guess) <= guess and guess < num_to_guess:
        status = 'Oops, your number is a little too small.'
        if current_guesses == max_guesses: max_guesses_guessed(max_guesses, num_to_guess)
        else:
            current_guesses += 1
            create_guess_entry(num_to_guess, max_guesses, current_guesses, status)   

    elif guess < num_to_guess:
        status = 'Oops, your number is too small.'
        if current_guesses == max_guesses: max_guesses_guessed(max_guesses, num_to_guess)
        else:
            current_guesses += 1
            create_guess_entry(num_to_guess, max_guesses, current_guesses, status)   

    elif guess == num_to_guess:
        num_guessed(num_to_guess, current_guesses)

    elif (guess - num_to_guess) <= (guess * 0.5) and guess > num_to_guess:
        status = 'Oops, your number is a little too big.'
        if current_guesses == max_guesses: max_guesses_guessed(max_guesses, num_to_guess)
        else:
            current_guesses += 1
            create_guess_entry(num_to_guess, max_guesses, current_guesses, status)

    elif guess > num_to_guess:
        status = 'Oops, your number is is too big.'
        if current_guesses == max_guesses: max_guesses_guessed(max_guesses, num_to_guess)
        else:
            current_guesses += 1
            create_guess_entry(num_to_guess, max_guesses, current_guesses, status)

def max_guesses_guessed(max_guesses, num_to_guess):
    label = tk.Label( # Creates loser label
        text = 'You have geuessed the maximum ({}) amount of guesses, the number was {}, better luck next time!\nPress enter to close'.format(max_guesses, num_to_guess)
    ); label.grid( # Grid label
        column = 1,
        row = 1
    ); window.bind('<Return>', lambda event: window.destroy()) # Bind enter quit

def num_guessed(num_to_guess, current_guesses):
    label = tk.Label( # Creates winner label
        text = 'Congradulations, you have geuessed the number ({}) in {} guesses!\nPress enter to close'.format(num_to_guess, current_guesses+1)
    ); label.grid( # Grid label
        column = 1,
        row = 1 
    ); window.bind('<Return>', lambda event: window.destroy()) # Bind enter to quit

if __name__ == '__main__':
    window = tk.Tk() # Create window
    fg = 'black' # Create universal fg colour
    bg = 'light gray' # Create universal bg colour
    window.title("Number Guessing Game") # Window title
    window.configure(background = bg) # Set window bg
    create_initial_entries() # First func
    window.mainloop() # Keeps window up
    quit()