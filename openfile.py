from pprint import pprint

name ='test_open_file.txt'
file = open(name, 'r')
pprint(file.read())
file.close()
