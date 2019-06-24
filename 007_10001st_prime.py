"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

prime_numbers = [2]
x = 3

while len(prime_numbers) < 10_001:
    for i in prime_numbers:
        if i > x ** 0.5:
            prime_numbers.append(x)
            break
        elif x % i == 0:
            break
        else:
            continue
    x += 2

print(prime_numbers.pop())
