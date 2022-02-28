def spelling_bee_solver(center_letter, around_letters):
    '''
    Takes in a list of letters str and a required letter str and returns a 
    list of words from wordlist that contains the required letter, with at
    least a length of 4, and do not contain any other letters not in the 
    letter_list.
    '''
    f = open('data/words.txt')  # Assume words.txt is under data folder

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z',]
    good_words = []

    for line in f:
        word = line.strip()
        if center_letter in word and len(word) > 3 and word not in around_letters:
            good_words.append(word)
    return good_words
