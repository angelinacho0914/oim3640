# import os
# print(os.getcwd())


# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# print(line)


# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True
    # return 'e' not in word.lower()

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    count = 0
    count_true = 0
    for line in f:
        word = line.strip()
        if has_no_e(word):
            count_true += 1
        count += 1
    return count_true/count


# perc_no_e = find_words_no_e()
# print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids_modified():
    """
    returns the number of words that don't contain any forbidden letters
    and print the number of words that don't contain any of them
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    
    forbidden = input('Please enter forbidden letters: ')
    count = 0

    for line in f:
        word = line.strip()
        for letter in word:
            if letter not in forbidden:
                count += 1
    return count


# print(avoids_modified())


def avoids(word, forbidden):
    '''
    takes a word and a string of forbidden letters, and that returns True 
    if the word doesn’t use any of the forbidden letters
    '''
    for letter in word:
        if letter.lower() in forbidden:
            return False
    return True


# print(avoids('Babson','abcde'))
# print(avoids('college','e'))
# print(avoids('Pop','xyz'))


def has_no_vowels(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    for letter in word:
        if letter.lower() in 'aeiou':
            return False
    return True

# print(has_no_vowels('Babson'))
# print(has_no_vowels('xYz'))
# print(has_no_vowels('cdf'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    count = 0
    count_true = 0
    for line in f:
        word = line.strip()
        if has_no_vowels(word):
            count_true += 1
        count += 1
    return count_true/count


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))
# print(uses_only('college', 'DfH'))


def find_words_only_use_planet():
    """
    """
    pass


# print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    # 1. iterate through the required string
    # 2.    if letter is not in a word:
    # 3.        return False
    # 4. return True
    for letter in required:
        if letter not in word:
            return False
    return True


# print(uses_all('Babson','asob'))
# print(uses_all('iPad','jqst'))
# print(uses_all('PureLeaf','uearC'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('data/words.txt')

    count = 0
    for line in f:
        word = line.strip()
        if uses_all(word,'aeiou'):
            count += 1
    return count


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    count = 0
    for count in range(len(word)-1):
        if word[count] > word[count+1]:
            return False
        count += 1
    return True


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    f = open('data/words.txt')

    count = 0
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            count += 1
    return count


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass

# print(is_abecedarian_using_while('abcdef'))