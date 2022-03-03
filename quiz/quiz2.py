def list_of_words():
    file = open('data/random_words.txt')
    count = 0
    number_of_words = 0
    for words in file:
        letters = words.split()
        if words[letters] in 'covid':
            count += 1
            if count >= 3:
                if words[letters] == words[letters+1]:
                    if words[0] == words[-1]:
                        number_of_words += 1
    return number_of_words
