a = [1, 2, 3, 4]
b = [7, 8, 9, 1, 2, 3, 5]
a.append(5)
a.extend(b)

a.insert(5, 6)
a.remove(2)
print(a.index(1, 0))
print(a.index(1, 6))
print(a.pop())
a.reverse()
print(a)
a.sort()
print(a)
print(a.count(10))
print(a.count(1))
print(a)
