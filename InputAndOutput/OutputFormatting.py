year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:1.3%}'.format(yes_votes, percentage))


import math
print(f'The value of pi is approximately {math.pi:.3f}.')

print('The value of pi is approximately %5.3f.' % math.pi)
