"""2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?

"""

from factors import prime_factors, smallest_multiply


all_factors = prime_factors(20)
for i in range(1, 20):
    all_factors = smallest_multiply(all_factors, prime_factors(i))


multiply = 1
for factor, reps in all_factors.items():
    multiply *= factor ** reps
print(multiply)
