def f(a=4, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f())


def f(a=4, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f())
print(f(5))
