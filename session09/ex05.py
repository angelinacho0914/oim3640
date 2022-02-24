# 'A' rotated by 3 is 'D' and 'Z' rotated by 1 is 'A'
# To rotate a word, rotate each letter by the same amount.
    # e.g. 'cheer' rotated by 7 is 'jolly' and 'melon' rorated by -10 is 'cubed'.

def rotate_word(word, n):
    '''
    Takes a string and an integer as parameters, and returns a
    new string that contains the letters from the original string
    rotated by the given amount.
    '''
    # iterating through the word
    # find out the unicode of the letter
    # add n amount to it
    # conver it (unicode) back to a character
    # repeat this for all the letters in the word
    # return the word
    word_list = ['']
    for letter in word:
        x = ord(letter)     # Use ord() which converts a character to a numeric code
        x += n
        word_list += chr(x)  # Use chr() which converts numeric codes to characters
    new_word = ''.join(word_list)
    return new_word



def main():
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))    # This actually prints out "c[bed"


if __name__ == "__main__":
    main()
