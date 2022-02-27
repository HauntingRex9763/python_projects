# Thanks, https://www.hangmanwords.com/words

import random
import tkinter as tk

class App(tk.Frame):
    def __init__(self, window):
        super(App, self).__init__()
        # Window setup
        fg = 'black'
        bg = 'light gray'
        window.geometry("3000x200")
        window.title("Hangman")
        window.configure(background = bg)

        # GAME VARS
        words_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
        strikes = 0 # Current strikes
        max_strikes = 5 # Max strikes
        selected_word = list(words_list[random.randint(0,len(words_list)-1)]) # Word selected to be guessed
        alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
        display_word = []
        for i in range(0, len(selected_word)):
            display_word.append('_')

        button_building(self, letter, strikes, max_strikes, selected_word, display_word, alphabet)
        
    def button_building(self, letter, strikes, max_strikes, selected_word, display_word, alphabet):
        for i in range(0,2): # Button building
            for j in range(0, 13):
                letter = alphabet[0] # Get letter 

                '''
                button_image = tk.PhotoImage(file = "rounded_square_sin_bg.png") # Gets image
                button_image = button_image.subsample(10, 10) # Crops image
                '''

                button = tk.Button( # Button Setup
                    window,
                    #image = button_image,
                    text = letter,
                    width = 5,
                    height = 2,
                    bg = "green",
                    fg = "yellow",
                    borderwidth = 0,
                    compound = tk.CENTER,
                    command = button_function
                )
                button.grid( # Button Placement
                    row = i, 
                    column = j, 
                    pady = 10, 
                    padx = 10
                )

                del(alphabet[0])

    def button_function(self, letter, strikes, max_strikes, selected_word, display_word, alphabet):
        if letter not in selected_word:
            strikes +=1
            if strikes == max_strikes:
                end_game()

        while letter in selected_word:
            letter_loc = selected_word.index(letter)
            display_word[letter_loc] = letter
            selected_word[letter_loc] = '_'
        print(letter)

    def end_game():
        pass

    

    
if __name__ == '__main__':
    window = tk.Tk() # Creates the window which will host widgets

    app = App(window).pack(side="top", fill="both", expand=True)

    window.mainloop() # Anything below this will not be executed until window is closed































'''      


label_ex = tk.Label(
    text = 'Welcome to Hangman', # Creates a label which welcomes the user to the game
    foreground = fg,  # Set the text color
    background = bg,  # Set the background color
    height = 1,
    width = 18
    font = ('Verdana', 15)
); label_ex.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Adds the label to the window, and sizes window to label

button_image = tk.PhotoImage(file = "rounded_square_sin_bg.png")

button_ex = tk.Button(
    window,
    image = button_image,
    text = letter,
    width = 20,
    height = 20,
    bg = "green",
    fg = "yellow",
    borderwidth = 0,
    command = button_function(letter)
); button_ex.grid(
    row = r, 
    column = c, 
    pady = 10, 
    padx = 10
)
'''