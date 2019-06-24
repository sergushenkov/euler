"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

x = 600851475143
factor = 2
while factor <= x ** 0.5:
    if x % factor != 0:
        factor += 1
    else:
        x //= factor
print(x)
