# Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел

import time

def time_now():
    return round(time.time()%1000)

numb = int(input('Enter your number: '))
tmp = 1
list = []
for i in range(numb):
    list.append((tmp*time_now())//10)
    list.append(((tmp*time_now())//10)//3)
    list.append(((tmp*time_now())//10)//2)
    tmp += 2
print(list)
    
