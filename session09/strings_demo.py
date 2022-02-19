# # continue - done with the current iteration, and jump on 
# #   to the next iteration


# # Index
# team = 'New England Patriots'
# letter = team[1] # The expression in brackets is called an index
# print(letter)

# # Q: What's the first letter? A: Index 0
# print(team[0])
# # print(team[1.5]) # It will show TypeError


# # len
# print(len(team))

# # Find the last letter?
# last = team[len(team)-1]
# print(last)

# # Another way to find the last letter
# last = team[-1]
# print(last)


# # Traversal loop
#     # while loop
# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index += 1

#     # for loop
# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     print(letter + suffix)


# print(team[0:11])
# print(team[12:20])

# # If you omit the first index (before the colon), the slice
# #   starts at the beginning of the string.
# # if you omit the 2nd index, the slice goes to the end of the string.
# print(team[:11])
# print(team[12:])

# # team[:] A string slice can take a 3rd index that specifies the
# # "step size"; that is, the number of spaces between successive 
# # characters.
# # A step size of 2 means every other character; 3 means every third
# team[::2]


# # Error: Strings are immutable, can't change an existing string
# # team[12:20] = 'Seahawks'

# # Create a new string that is a variation on the original
# new_team = team[:12] + 'Seahawks'  # It has no effect on the string team
# print(new_team)

# # Searching
# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find(team, 'E'))


# # Looping and counting
# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count += 1
# print(count)


# # String methods
# team = 'New England Patriots'
# new_team = team.upper()         # Return the string to all uppercase letter
# print(new_team)

# index = team.find('a')          # Find both upper and lower case "A"
# print(index)
# print(team.find('En'))          # The number is the location of "E"
# print(team.find('a', 10))
# print(team.find('E', 2, 10))    # .find(sub, start, end)


# The in operator
# in is a boolean operator that takes 2 strings and returns True
#   if the first appears as a substring in the second:
team = 'New England Patriots'
print('a' in team) # print True
print('Boston' in team) # print False