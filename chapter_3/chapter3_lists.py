wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
print(wizard_list)
print(wizard_list[2])

wizard_list[2] = 'язык улитки'
print(wizard_list)

print(wizard_list[2:5])

numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь']
print(numbers_and_strings)

numbers = [1, 2, 3, 4, 5]
strings = ['хватит', 'циферки', 'считать']
mylist = [numbers, strings]
print(mylist)

wizard_list.append('медвежий коготь')
print(wizard_list)

wizard_list.append('мандрагора')
wizard_list.append('болиголов')
wizard_list.append('болотный газ')
print(wizard_list)

del wizard_list[5]
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

list1 = [1, 2, 3, 4, 5]
list2 = ['я', 'забрался', 'под', 'кровать']
print(list1 + list2)

list1 = [1, 2, 3, 4]
list2 = ['я', 'мечтаю', 'о', 'пломбире']
list3 = list1 + list2
print(list3)

list1 = [1, 2]
print(list1 * 5)