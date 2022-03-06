def list_of_words():
    file = open('data/random_words.txt')
    count = 0
    number_of_words = 0

    for words in file:
        letters = list(words)
        # print(letters) # Checked it's correctly separated
        for i in range(len(letters)):
            if letters[i] in 'covid':
                count += 1
        if count >= 3:
            for i in range(len(letters)-1):
                if letters[i] == letters[i+1]:
                    if letters[0] == letters[-1]:
                        number_of_words += 1
    return number_of_words

print(list_of_words())
