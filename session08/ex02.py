# # The While statement
# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff!')

# # ex02-01
# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every
#     # character, including spaces and commas!
#     for letter in "hello, world":
#         count += 1
#     print(f"Iteration {str(iteration)}; count is: {str(count)}")
#     iteration += 1

#     # 1. What is the value of the variable count that's printed out
#     #   on iteration 0?
#     # count = 12 (12 characters in hello, world)
#     # 2. What is the value of the variable count that's printed out
#     #   on iteration 1?
#     # 3. count = 24
#     # 4. count = 36
#     # 5. count = 48
#     # 6. count = 60


# # ex02-02
# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print(f"Iteration {str(iteration)}; count is: {str(count)}")
#     iteration += 1

#     # 1. iteration 0; count 12
#     # 2. iteration 1; count 12
#     # 3. iteration 2; count 12
#     # 4. iteration 3; count 12
#     # 5. iteration 4; count 12


# # ex02-03
# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print(f"Iteration {str(iteration)}; count is: {str(count)}")
#     iteration += 1

#     # 1. The print statement will be executed 5 times.
#     # 2. The largest value of iteration will be 4.
#     # 3. The largest value of count will be 12.
#     # 4. The smallest value of count will be 1.


while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')