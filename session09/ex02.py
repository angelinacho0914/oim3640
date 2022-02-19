# Encapsulate this code in a function named count, and
# generalize it so that it accepts the string and the 
# letter as arguments.


def count(word, letter):
    '''
    Takes in the word and letter wanted to find as parameters,
    and print the number of times the letter appears in the word.
    '''
    count = 0
    for i in word:
        if i == letter:
            count += 1
    print(count)


def main():
    count('geez', 'e')

if __name__ == "__main__":
    main()