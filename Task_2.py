#  Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def find_idx_sec_entry(list_in: list, str_in: str):
    count = 0
    result = -1
    for i in range(len(list_in)):
        if list_in[i] == str_in:
            count += 1
            if count == 2:
                result = i                        
    return result

my_list = input('Enter your strings: ').split()
print('Your list:', my_list)
my_string = input('Enter your string to find: ')
my_index =  find_idx_sec_entry(my_list, my_string)
if my_index != -1:
    print('Your index of the second entry:', my_index)
else:
    print('There is no second entry')
