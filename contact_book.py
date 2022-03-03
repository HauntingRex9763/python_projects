import tkinter as tk, openpyxl
'''
    Contact management program, with automated messages. 
    Per person collect:
    First, Middle, Last # Row 1, 2, 3
    email # Row 4
    phone # Row 5
    Birthday (Y,M,D) # Row 6, 7, 8
    image # Row 9
    '''
def make_entry(r, c):
    var = tk.IntVar()
    entry = tk.Entry( 
        width = 20
    ); entry.grid(
        row = r,
        column = c
    ); entry.focus()
    window.bind('<Return>', lambda event: var.set(1))
    window.wait_variable(var)
    out_var = entry.get()
    for widget in window.winfo_children():  widget.destroy() # Clear widgets
    return(out_var)

def make_label(_text, r, c):
    label = tk.Label(
        text = _text
    ); label.grid(
        row = r, 
        column = c
    )

def main_1():
    for widget in window.winfo_children():  widget.destroy() # Clear widgets  
    

    def create_button(_text, cmd, r, c):
        button = tk.Button( # Button Setup
            window,
            text = _text,
            width = 15,
            height = 2,
            bg = "green",
            fg = "yellow",
            borderwidth = 3,
            compound = tk.CENTER,
            command = cmd
        ); button.grid( # Button Placement
            row = r, 
            column = c
        ); return(button)

    def main_1_A():
        for widget in window.winfo_children():  widget.destroy() # Clear widgets  
        make_label('Enter contact email.\nPress enter to continue.', 1, 2) # Post label  
        entry = make_entry(1, 1); var = False # Get email
        
        for row in range(2, ws.max_row+1): # Find email
            if ws['D'+str(row)].value == entry:
                ws.delete_rows(row); var = True
                make_label('Contact removed.\nPress enter to go back to main menu.', 1, 1)
                window.bind('<Return>', lambda event: main_1()) # Bind enter to entry get_func
                
        if var == False: make_label('Contact not found.\nPress enter to go back to main menu.\n{}', 1, 1)
        window.bind('<Return>', lambda event: main_1()) # Bind enter to entry get_func

    def main_1_B():
        for widget in window.winfo_children():  widget.destroy() # Clear widgets
        contacts = 'Here is all submitted contact information.\n' # Gets contacts
        for r in range(2, ws.max_row+1):
            for c in range(1, 10):
                contacts += '{} : {}; '.format(ws.cell(row=1, column=c).value, ws.cell(row=r, column=c).value)
            contacts += '\n'
        contacts += '\nPress enter to return to main page.'
        make_label(contacts, 1, 1) # Post contacts
        window.bind('<Return>', lambda event: main_1()) # Bind enter to entry get_func

    def main_1_C():
        for widget in window.winfo_children():  widget.destroy() # Clear widgets    
        make_label('Enter email.\nPress enter to continue.', 1, 2) # Posts label
        entry = make_entry(1, 1) # Gets email

        ws['J1'] = entry # Add email to sheet
        make_label('Email: {} added.\nPress enter to continue.'.format(entry), 1, 2) # Post label
        window.bind('<Return>', lambda event: main_1()) # Bind enter to main func
        
    def main_1_D():
        try:  
            wb.save(filename = 'contact_book.xlsx')
            window.quit()
        except Exception as e:
            print("OPENPYXL IS A PIECE OF SHIT\n",e)

    add_button = create_button('Add contact', first_name_1, 1, 1)

    remove_button = create_button('Remove contact', main_1_A, 1, 2)
        
    view_button = create_button('View contact', main_1_B, 1, 3)

    quit_button = create_button('Add personal email', main_1_C, 1, 4)
       
    quit_button = create_button('Quit', main_1_D, 1, 5)

def first_name_1():
    for widget in window.winfo_children():  widget.destroy() # Clear widgets    
    make_label('Enter first name.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get first
    ws['A'+str(ws.max_row+1)] = str(entry) # Add first
    middle_name_1() # Next

def middle_name_1(): 
    make_label('Enter middle name.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get middle
    ws['B'+str(ws.max_row)] = str(entry) # Add middle
    last_name_1() # Next

def last_name_1(): 
    make_label('Enter last name.\nPress enter to continue.', 1, 2)
    entry = make_entry(1, 1) # Get last
    ws['C'+str(ws.max_row)] = str(entry) # Add last
    email_1() # Next

def email_1(): 
    make_label('Enter email.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get email
    ws['D'+str(ws.max_row)] = str(entry) # Add email
    phone_1() # Next

def phone_1(): 
    make_label('Enter phone number.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get phone
    ws['E'+str(ws.max_row)] = str(entry) # Add phone
    birth_year_1() # Next

def birth_year_1():    
    make_label('Enter birth year.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get year
    ws['F'+str(ws.max_row)] = int(entry) # Add year
    birth_month_1() # Next
    
def birth_month_1(): # First
    make_label('Enter birth month.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get month
    ws['G'+str(ws.max_row)] = int(entry) # Add month
    birth_day_1() # Next

def birth_day_1(): # First 
    make_label('Enter birth day.\nPress enter to continue.', 1, 2) # Post label
    entry = make_entry(1, 1) # Get day
    ws['H'+str(ws.max_row)] = int(entry) # Add day
    image_1() # Next

def image_1(): 
    make_label('Enter image path.\nPress enter to continue.', 1, 2) # Post label  
    entry = make_entry(1, 1) # Get image path

    image = openpyxl.drawing.image.Image(entry) # Get image
    image.height = 20
    image.width = 72
    image.anchor = ''+str(ws.max_row) # Attach to cell
    ws.add_image(image) # Add
    results_1() # Next

def results_1():
    contact = 'Here is submitted conact info.\n' # Get contact
    for i in range(1, ws.max_column-1): 
        contact += '{}\n'.format(ws.cell(row=ws.max_row, column=i).value)
    contact += '\nPress enter to return to main page.'
    make_label(contact, 1, 1) # Post label
    window.bind('<Return>', lambda event: main_1()) # Bind enter to entry get_func
    
if __name__ == '__main__':
    # Excel setup
    wb = openpyxl.load_workbook('contact_book.xlsx')
    
    ws = wb['contact_book']
    alph = list('abcdefghijklmnopqrstuvwxyz')

    # Window creation
    window = tk.Tk() # Create window
    fg = 'black'
    bg = 'light gray' 
    window.title("Contact Book")
    window.configure(background = bg)

    main_1() # First func

    window.mainloop() # Keeps window up 