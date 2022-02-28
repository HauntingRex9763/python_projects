import datetime, time, playsound, tkinter as tk # Import necesary functions

def set_alarm_button_func():    
    set_alarm_button = tk.Button( # Create button 
        window, # Button's window
        text = 'Set Alarm', # Button label
        width = 10, # Button width (0)
        height = 1, # Button height (0)
        bg = "green", # Button bg
        fg = "yellow", # Button fg
        borderwidth = 0, # Button border
        command = lambda: set_alarm_entry_func(set_alarm_button) # Button function
    ); set_alarm_button.pack() # Size the screen to button

def set_alarm_entry_func(set_alarm_button): # Create entry displpay func
    set_alarm_button.pack_forget() # Remove button

    set_alarm_entry = tk.Entry( # Crete entry
        window, # Enty's window
        background = bg, # Entry bg
        width = 5, # Entry width
        border = 1, # Entry border
        cursor = 'dot', # Entry curser type
        foreground = fg, # Entry fg
    ); set_alarm_entry.pack() # pack window to entry size
    window.bind('<Return>', lambda event: get_alarm_entry_func(set_alarm_entry)) # Bind enter to entry get func
                                                                                                        
def get_alarm_entry_func(set_alarm_entry): # Entry get func
    window.unbind('<Return>'); # Unbind return

    alarm_time = set_alarm_entry.get() # Get entry
    now = datetime.datetime.now() # Get time
    while(int(alarm_time.split(':')[0]) != now.hour or int(alarm_time.split(':')[1]) != now.minute): # If entered time ! current time
        time.sleep(50) # Wait 50s
        now = datetime.datetime.now() # Update current time
    playsound.playsound('alarm_clock_audio.wav') # Play audio file
    set_alarm_entry.pack_forget() # Remove entry
    window.quit() # Close window

window = tk.Tk() # Create window
fg = 'black' # Create universal fg colour
bg = 'light gray' # Create universal bg colour
window.title("Alarm Clock") # Window title
window.configure(background = bg) # Set window bg
set_alarm_button_func()

window.mainloop() # Keep screen up