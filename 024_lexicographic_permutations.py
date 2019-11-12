"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

def all_permutation(source, permutation, list_permutation):
    if len(source) == 0:
        list_permutation.append(int(permutation))
    else:
        for i in range(len(source)):
            all_permutation(source[:i] + source[i+1:], permutation + source[i], list_permutation)
            
list_permutation = []
all_permutation('0123456789', '', list_permutation)
list_permutation.sort()
print(list_permutation[999_999])
