#Дано целое число N (>0) и строка S. Преобразовать строку S в строку длины N
#следующим образом: если длина строки S больше N, то отбросить первые символы,
#если длина строки S меньше N, то в ее начало добавить символы «.» (точка).


n = int(input('введи число: '))
s = 'HELLO WORLD'
sdlinan = len(s)

if n < 0:
    print("введите не меньше нуля")

#если dlina str S > N
else:

    if len(s) > n:
        print(s[n:])

    else:
        dot = '.' * n
        print(dot+s)




