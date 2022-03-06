def store_words():
    '''
    Store the strings in words.txt into a dictionary and return the dictionary
    '''
    file = open('data/words.txt')
    words_dict = dict()
    for line in file:
        words = line.strip()
        if words not in words_dict:
            words_dict[words] = 1
    return words_dict

# print(store_words())  # Check store_words function


def has_duplicates(words_list):
    d = dict()
    for i in range(len(words_list)):
        if words_list[i] not in d:
            words = words_list[i]
            d[words] = 1
        else:
            words = words_list[i]
            d[words] += 1
    if 2 in d.values():
        return True
    return False

appeared_words = ['babson', 'angelina', 'class', 'better', 'babson']
print(has_duplicates(appeared_words))


