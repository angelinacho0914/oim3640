# How many vowels are there in your name?

def vowels(name):
    count = 0
    for letter in name:
        if letter in 'aeiou':
            count += 1
    return count

print(vowels('Angelina Cho'))