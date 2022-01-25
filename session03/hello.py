name = input()
print("Hello, ", name)

a = 123  # a is an integer
print(a)
a = "ABC"  # a becomes a string)
print(a)

x = 10
x = x + 2  # This does not make sense in mathematics,
# but it is perfectly ok in Python.
print(x)

a = "ABC"
b = a
a = "XYZ"
print(b)

actor = "Joaquin Phoenix"
year = 2020
movie = "Joker"
print(f"{actor} wins Best Actor for {movie} at Golden Globes {year}.")

pi = 3.1415926
print(f"Pi equals {pi:.5f}.")
print(f"Pi equals {pi:8.5f}.")
print(f"Pi equals {pi:8.2f}.")

a = 2021
# binary
print(f"{a:b}")
# hexadecimal
print(f"{a:x}")
# octal
print(f"{a:o}")
# scientific
print(f"{a:e}")

s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')

print("na na na na\n" * 3)
