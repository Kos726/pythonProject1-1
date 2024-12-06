from pprint import pprint

name = 'file.txt'
file = open(name, 'r') # r, w, a = read, write, append
print(file.read())
file.close()

name2 = 'file2.txt'
file = open(name2, 'w') # r, w, a = read, write, append
file.write('Hello World!')
file.close()

name3 = 'file2.txt'
file = open(name3, 'a') # r, w, a = read, write, append
file.write('\nHello World!!!')
file.close()


name4 = 'file2.txt'
file = open(name4, 'r') # r, w, a = read, write, append
print(file.tell())
pprint(file.read())
print(file.seek(20))
pprint(file.read())
file.close()