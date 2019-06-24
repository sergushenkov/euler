"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

prime_numbers = [2]
x = 3

while x < 2_000_000:
    for i in prime_numbers:
        if i > x ** 0.5:
            prime_numbers.append(x)
            break
        elif x % i == 0:
            break
        else:
            continue
    x += 2

print(sum(prime_numbers))
