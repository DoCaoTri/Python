tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
{'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

a = {x: x**2 for x in (2, 3, 6)}
print(a)

b = dict(sape=4129, guido=4127, jack=4098)
print(b)
