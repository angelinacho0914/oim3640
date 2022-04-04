# fout = open('data/dylan.txt', 'a')  # a - addition, w - write
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)

# line2 = "Before you all him a man?\n"
# fout.write(line2)
# fout.close()


# "with" automatically closes the file after this
with open('data/dylan.txt', 'w') as fout:
    line1 = "How many roads must a man walk down\n"
    fout.write(line1)
    line2 = "Before you all him a man?\n"
    fout.write(line2)


from cmath import e
import os
cwd = os.getcwd()   # returns the name of the current directory
# cwd stands for "current working directory"
print(cwd)

# os.path provides other functions for working with filnames and paths
os.path.abspath('dylan.txt')
os.path.exists('dylan.txt')
os.path.iddir('dylan.txt')
os.psth.isdir('/exercises')
os.path.isfile('dylan.txt')
os.listdir(cwd)

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# walk(os.getcwd())


# Catching exceptions
try:
    f = open('data/data.txt')
except Exception as e:
    print(e)

print('hello, world!')


# Pickling
import pickle
t = [1, 2, 3]
s = pickle.dumps(t)
t2 = pickle.loads(s)
print(t2)