parol = input ('Введите пароль: ')
result = 0

try:
     length = len(parol)
     proverka =  100 / length
     try:
         int (parol)
         print ('Ваш пароль состоит только из цифр')
     except ValueError:
         print ('Требования к паролю соблюдены')  
except ZeroDivisionError:
     print('Вы ввели пустой пароль')

    