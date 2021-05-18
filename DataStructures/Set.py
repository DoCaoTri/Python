basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a = set(('abracadabra', 'alacazam'))
print(a)

b = {x for x in 'abracadabra' if x not in 'abc'}
print(b)
