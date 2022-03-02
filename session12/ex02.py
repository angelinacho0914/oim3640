t = ['a', 'b','c']
t.append('d') # Adds 'd' into the end of the list t
print(t)

p = ['e', 'f','g']
t.extend(p) # Adds items into the end of the list
t.extend(p) # Adss a whole list as a single item at the end of the list
print(t)

t.insert(2, 1) # Insert int'1' in the list at index 2
print(t)