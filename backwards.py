'''
Make Backwards, by Jackson Urquhart - 19 February 2022 @ 23:43
'''

in_str = str(input("\nEnter phrase: \n")) # Gets in_string from user
order = str(input("\nKeep order of words? y/n \n")) # Gets order from input

def main(in_str, order): # Creates main function
    out_str = '' # Create local out_str

    if order=='y':
        for word in in_str.split():
            for letter in reversed(word): # For letter in in_str, from back to front (i--)
                out_str += letter # Add letter to out_str
            out_str += ' ' # Add space at end of word
    else:
        for letter in reversed(in_str): # For letter in in_str, from back to front (i--)
            out_str += letter # Add letter to out_str
            
    return(out_str) # Return out_str

out_str=main(in_str, order) # Create out_str 
print(out_str) # Print out_str