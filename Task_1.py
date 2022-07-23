# Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

def find_symb(list_in: list, symb: str):
    list_out = []
    for item in list_in:
        if symb in item:
            list_out.append(item)
    return list_out               
    

my_list = input('Enter your strings: ').split()
print('Your list:', my_list)
numb = input('Enter your number: ')
new_list =  find_symb(my_list, numb)
if new_list != []:
    print('Your number is contained here:', new_list)
else:
    print('Your number is not contained in this list')
