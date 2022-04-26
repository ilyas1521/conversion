#перевод
from collections import Counter
a = 9**8+3**5-2
# число которое переводим(10)
s = 3 # куда
o = ''# результат перевода
alf = '0123456789ABCDEF'
while a > 0:
    o = alf[a%s] + o
    a = a//s

print(Counter(o))

