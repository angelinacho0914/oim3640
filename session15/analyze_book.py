import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    sum_words = 0
    for v in hist.values():
        sum_words += v
    return sum_words
    # return sum(hist.values()) # This also works


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist.keys())


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    lst = []
    for word, freq in hist.items():
        if word not in process_file('data/stopwords.txt',skip_header=False):
            lst.append((freq,word))
    lst.sort(reverse=True)
    return lst


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    lst = most_common(hist)
    print(lst[0])


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    d = dict()
    for word_in_book in d1:
        print(word_in_book)
        if word_in_book not in d2:
            d[word_in_book] = 1
    return d


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    return random.choice(list(hist))


def main():
    hist = process_file('data/Pride and Prejudice.txt', skip_header=True)
    # print(hist)
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    # t = most_common(hist, excluding_stopwords=True)
    # print('The most common words are:')
    # for freq, word in t[0:20]:
    #     print(word, '\t', freq)
    # print_most_common(hist)

    # words = process_file('data/words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()