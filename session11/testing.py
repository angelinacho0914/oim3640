f = open('data/words.txt')
line = f.readline()
wordlist = []
for word in f:
        wordlist.append(str(word).lower()[:-1])


def solver(center_letters, around_letters):
    all_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z',]
    unused_letters = [x for x in all_letters if x not in around_letters]
    qualified_words = []

    for word in f:
        if center_letters in word.lower() and len(word) > 3:
            if any(unused_letters in word.lower() == False): 
                qualified_words.append(word)
    return qualified_words


required_letter = 'o'
list_of_letters = ['w','i','n','p','g','h']
print(solver(required_letter, list_of_letters))
