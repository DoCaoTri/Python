# open(filename, mode)

f = open("/home/tri/Exercise/Python/Python/InputAndOutput/testdoc.txt", "r+")
# print(f)
# print(f.read())

# with open('/home/tri/Exercise/Python/Python/InputAndOutput/testdoc.txt') as f:
#     read_data = f.read()
#     print(read_data)
print(f.readline())
print(f.readline())
print(f.readline())
print(f.write('\nThis is a test\n'))