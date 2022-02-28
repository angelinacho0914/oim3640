def spelling_bee_solver(letter_list, required_letter):
    '''
    Takes in a list of letters str and a required letter str and returns a 
    list of words from wordlist that contains the required letter, with at
    least a length of 4, and do not contain any other letters not in the 
    letter_list.
    '''
    f = open('data/words.txt') 

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z',]
    unused_letters = [x for x in alphabet if x not in letter_list]
    good_words = []

    for line in f:
        word = line.strip()
        if len(word) > 3:
            if required_letter in word:
                if word not in letter_list:
                        if any(x in unused_letters for x in word) == False:
                            good_words.append(word)
    return good_words





def main():
    list_of_letters = ['w','i','n','p','g','h','o']
    required_letter = 'o'
    print(spelling_bee_solver(list_of_letters, required_letter))


if __name__ == '__main__':
    main()
