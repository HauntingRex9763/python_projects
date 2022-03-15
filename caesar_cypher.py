'''
Caesar Cypher, by Jackson Urquhart - 19 February 2022 @ 22:47
'''

in_str = str(input("\nEnter phrase: \n")) # Gets in_string from user
key = int(input("\nEnter key: \n")) # Gets key from user
keep_upper = str(input("\nMaintain case? y/n\n")) # Determines whether user wants to maintiain case values

def encrypt(in_str, key): # Def encrypt
    out_str = '' # Object to be returned
    for letter in in_str: # For string in in_str
        if 96 < ord(letter.lower()) < 123: # If letter is a letter
            if keep_upper=='y' and letter.isupper(): # If letter is upper
                upper_status = True # Set upper_status to True

            letter=letter.lower()
            char=ord(letter) # Set char to ascii of letter
            char += key # Add key to ascii of letter

            if char>122: # If char with key is > 122 (z)
                print(char)
                char = 97+(123-char) # Subtract 123 from char and add additional value to 97 (a)
                print(char)

            if upper_status is True: # If letter is upper
                char -= 32 # Make char ASCII for uppper letter
                upper_status = False # Reset upper status

            out_str += chr(char) # Add str value of char to out_str

        else: # If letter is not a letter
            out_str += letter # Add letter

    return(out_str) # Return out_str

out_str=encrypt(in_str, key) # Defines out_str as the reslt of  main
print(out_str) # Print out_str
        
