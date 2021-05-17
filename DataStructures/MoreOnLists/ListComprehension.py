squares = list(map(lambda x: x**2, range(10)))
print(squares)

list = [x**2 for x in range(10)]
print(list)

a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(a)

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([[num for num in elem] for elem in vec])

b= [sum(elem) for elem in vec]
print(b)

