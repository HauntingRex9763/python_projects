# Card Flip Trick, by Jackson Urquhart - 20 February 2022 @ 18:52


# Creates the deck
deck=[[["Ace of Hearts",1010],["2 of Hearts",1011],["3 of Hearts",1012],["4 of Hearts",1013],["5 of Hearts",1014],["6 of Hearts",1015],["7 of Hearts",1016],["8 of Hearts",1017],["9 of Hearts",1018],["10 of Hearts",1019],["Jack of Hearts",1020],["Queen of Hearts",1021],["King of Hearts",1022]],
      [["Ace of Diamonds",2010],["2 of Diamonds",2011],["3 of Diamonds",2012],["4 of Diamonds",2013],["5 of Diamonds",2014],["6 of Diamonds",2015],["7 of Diamonds",2016],["8 of Diamonds",2017],["9 of Diamonds",2018],["10 of Diamonds",2019],["Jack of Diamonds",2020],["Queen of Diamonds",2021],["King of Diamonds",2022]],
      [["Ace of Spades",3010],["2 of Spades",3011],["3 of Spades",3012],["4 of Spades",3013],["5 of Spades",3014],["6 of Spades",3015],["7 of Spades",3016],["8 of Spades",3017],["9 of Spades",3018],["10 of Spades",3019],["Jack of Spades",3020],["Queen of Spades",3021],["King of Spades",3022]],
      [["Ace of Clubs",4010],["2 of Clubs",4011],["3 of Clubs",4012],["4 of Clubs",4013],["5 of Clubs",4014],["6 of Clubs",4015],["7 of Clubs",4016],["8 of Clubs",4017],["9 of Clubs",4018],["10 of Clubs",4019],["Jack of Clubs",4020],["Queen of Clubs",4021],["King of Clubs",4022]]]

def shuffle(deck): # Function to huffle deck, and remove suit list
    deck_in_play=[] # Creates deck to be played
    for i in range(0,4): # For suit in deck
        for j in range(0,13): # For card in suit
            deck_in_play.append(deck[i][j]) # Add card to deck_in_play
    random.shuffle(deck_in_play) # Shuffle deck_in_play
    return deck_in_play # Return to_in_play

def get_packets(deck): # Function to get a list of packets, and at the end of list rest of deck
    packets = [] # Create the variable packets will be stored in
    while True: # Runs until there is not enough cards left in the deck to create next packet
        packet = [] # Create empty packet    
        card_num = int(str(deck[0][1])[2:4]) # Get value of first card flipped
        
        if len(deck) > 23-card_num: # If deck has diffrence for next packet
            for i in range(card_num, 23): # From value of first card flipped, count to 13
                packet.append(deck[0]) # Add card to packet
                del(deck[0]) # Delete card from deck
            packets.append(packet) # Add packet to packets
            
        else:
            packets.append(deck) # Add rest of deck to packets as packet
            break # Exits the loop
        
    return(packets) # Returns packets

def select_packets(packets):
    packets_kept = [] # Creates variable that will contain packets kept by player
    
    for i in range(0,3): # For number of packets to be kept
        packet_to_keep = random.randint(0,len(packets)-2) # This subtract two from len because player cannot choose rest of deck, which is at the end of the packets list 
        packets_kept.append(packets[packet_to_keep]) # Add random packet to deck, or could let player decide
        del(packets[packet_to_keep]) # Delete selected packet from packets

    packet_left = [] # This variable will have all leftover packets stacked on them
    for packet in packets: # For packet left in packets
        for card in packet: # For card in packets
            packet_left.append(card) # Add card to packet_left (this structure stacks packets on top of eachother )

    return(packets_kept, packet_left) # Returns packets_kept, packet_left

def run_trick(packets_kept, packet_left): # Final phase
    discard_packet = [] # Packet that packet_left will be discarded to
    for i in range(0,10): # Loop ten times
        discard_packet.append(packet_left[-1]) # Add top card to discard_packet
        del(packet_left[-1]) # Delete top card from packet
    for packet in range(0,2): # Loop twice
        card_flipped = int(str(packets_kept[packet][0][1])[2:4])-9 # Top card off first/second packet
        for i in range(0, card_flipped): # For the value of the card
            discard_packet.append(packet_left[-1]) # Add top card to discard packet
            del(packet_left[-1]) # Delete top card from packet_left
            
    print('Gee, I do not have many cards left here... only', len(packet_left),'how many cards are left in your final packet?') # Shows result
    print(str(packets_kept[2][0][0])+'?! Holy smokes, that is just enough!!!') # Shows result
     



import random # Import random library

# Setup
deck = shuffle(deck) # Shuffles deck
packets = get_packets(deck) # Gets a list of packets, and at the end of list rest of deck
packets_kept, packet_left = select_packets(packets) # Gets a list of packets player kept, then a list of all remaining cards in proper order

# this_is_where_the_fun_begins.png
run_trick(packets_kept, packet_left)
