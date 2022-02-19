# Modify the program to fix the names of Ouack and Quack

prefixes = 'JKLMNOPQ'
suffix = 'ack'
suffix2 = 'uack'
for letter in prefixes:
    if letter == 'Q' or letter == 'O':
        print(letter + suffix2)
    else:
        print(letter + suffix)