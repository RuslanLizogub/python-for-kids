# Strings
fred = "Почему у горилл большие ноздри? Потому что у них толстые пальцы!"
print (fred)
fred = 'Что это: розовое и пушистое? Розовый пушистик!'
print(fred)
fred = '''Что едят наполдник динозавры?
ТиРекс-кекс!'''
print(fred)
silly_string = ''' ""Тут что-то не так, не будь я д'Артаньян" —  подумал он. '''
print(silly_string)
silly_string = "\"Тут что-то не так, не будь я д\'Артаньян\" —  подумал он."
print(silly_string)

myscore = 1000
myscore2 = 2000
message = 'Мой счет: %s очков'
print(message % myscore)
print(message % myscore2)
print(message % 3000)

nums = 'Что сказало число %s числу %s? Славный поясок!'
print(nums % (0, 8))

print(10 * 'a')