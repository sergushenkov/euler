"""
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

# считываю имена из файла в отсортированный список
with open('p022_names.txt') as f:
    names = f.read().strip().split(',')
    names.sort()

# создаю словарь для расчета числового значения имени
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 1
char_dict = dict()
for char in alphabet:
    char_dict[char] = count
    count += 1
    
# перебирая имена из списка, высчитываю числовое значение и 
# умножаю его на порядковый номер имени
total_score = 0
count = 1
for name in names:
    name_score = 0
    for char in name.lower()[1:-1]:
        name_score += char_dict[char]
    total_score += name_score * count
    count += 1
    
print(total_score)       