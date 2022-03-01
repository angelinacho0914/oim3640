from word import uses_all, uses_only


def solver(center_letters, around_letters):
    f = open('data/words.txt')
    qualified_words = []

    for line in f:
        word = line.strip()
        if len(word) > 3 and uses_only(word, around_letters) and uses_all(word, center_letters):
            qualified_words.append(word)
    return qualified_words

def main():
    required_letter = 'o'
    list_of_letters = ['w','i','n','p','g','h','o']
    print(solver(required_letter, list_of_letters))

if __name__ == "__main__":
    main()
