import fibo 

fibo.fib(1000)

print(fibo.fib2(100))

print(fibo.__name__)

from fibo import fib, fib2
fib(500)

from fibo import *

import fibo as fib

from fibo import fib as fibonacci
fibonacci(500)