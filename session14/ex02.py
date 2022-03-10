from ctypes.wintypes import WORD


def most_frequent(letters):
    '''
    Takes a string and prints the letters in decreasing order of letter frequency.
    '''
    # 1. read string into a list of letters
    # 2. sort the string and convert the word to a sorted list or tuple
    # 2.5 have a dictionary  
    # 3. iterate it and put it inversely into a new list or tuple
    d = dict()
    for l in letters:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    # .items()displays a list of given dict's tuple pair, key is a way to call in line function, lambda is a no name function, item:item[1] is a way of calling the items.
    return dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
    

print(most_frequent('dejeifeeef'))
print(most_frequent('aaaa'))
print(most_frequent('bbdggggsssssttt'))


'''
1. read words.txt into a list of words
2. sort one word, convert the word to a sorted tuple/string
3. create a dictionary, key is the sorted tuple/string, value is a list of anagram words

{'ab':['ab','ba',], 'opts':['stop','pots']}
4. create a new list, by getting the values of dict only - we only want to get the lists that have more than one word
5. print the list
'''

'''
print the longest:
{2:[['spot','pots'], ['ab','ba']]}
'''
def anagrams():
    f = open('data/words.txt')
    lst = list()
    d = dict()
    for line in f:
        word = line.strip()
        lst.append(word)
    for w in range(len(lst)-1):
        if w not in d:
            sorted_word = sorted(w)
            new_word = ''.join(sorted_word)
            d[new_word] = w
        if w in d:
            d[sorted(w)]
    pass

# Will work on this during the break.
            


anagrams()