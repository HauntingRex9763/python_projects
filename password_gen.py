# Password Generator by Jackson Urquhart - 28, February, 2022 10:13

import tkinter as tk, random

def func_1(): # First
    def func_1_A(): # First extension
        password_length = int(entry.get()); entry.grid_remove(); label.grid_remove() # Get entry and remove widgets
        password = '' # Declare password
        password_chars = '1234567890[]\;\'\\,./~!@#$%^&*()_+{}|:"<>?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<' # Chars
        for letter in range(0, password_length): # For requested len:
            password += password_chars[random.randint(0, len(password_chars))] # Add a char
        func_2(password) # Call display func

    entry = tk.Entry( # Create, label, and focus entry
        width = 20
    ); entry.grid(
        row = 1,
        column = 1
    ); label = tk.Label(
        text = 'How long do you want your password?\nPress enter to continue.'
    ); label.grid(
        row = 1, 
        column = 2
    ); entry.focus()
    window.bind('<Return>', lambda event: func_1_A()) # Bind enter to entry get_func

def func_2(password): # Second func
    label = tk.Label( # Return the generated password via label, and bind to quit
        text = 'Your generated password is: {}'.format(password)
    ); label.grid(
        row = 1,
        column = 1
    ); window.bind('<Return>', lambda event: window.quit())

if __name__ == '__main__':
    window = tk.Tk() # Create window
    fg = 'black' # Create universal fg colour
    bg = 'light gray' # Create universal bg colour
    window.title("Password Generator") # Window title
    window.configure(background = bg) # Set window bg
    func_1() # First func
    window.mainloop() # Keeps window up 