fibs = (0, 1, 1, 2, 3)
print(fibs[3])

# Dictionaries
favorite_sports = {'Ральф Уильямс': 'Футбол',
'Майкл Типпетт': 'Баскетбол',
'Эдвард Элгар': 'Бейсбол',
'Ребекка Кларк': 'Нетбол',
'Этель Смит': 'Бадминтон',
'Фрэнк Бридж': 'Регби'}
print(favorite_sports['Ребекка Кларк'])

del favorite_sports['Этель Смит']
print(favorite_sports)

favorite_sports['Ральф Уильямс'] = 'Хоккей на льду'
print(favorite_sports)
