import hashlib



def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

#valid password = vicare13
hash_password = 'f59406461b874c6fc4b3fe15b7b707fb3b242a8efbf9d414312a58692ae34f2f'

while True:
    input_password = input('input password here: ')
    hash_input_password = my_hash(input_password)

    if hash_password == hash_input_password:
        print('password valid!')
        break
    else:
        print('non valid password!!!')


#сделать чтобы хеш проходил автоматический



#
# def my_sum(a, b):
#     if a > b:
#         return a + b
#     else:
#         return a - b
#
#
# num1 = int(input("Введи 1 число"))
# num2 = int(input("Введи 2 число"))
# print("результат = ", my_sum(num1, num2))


# def my_sum(a, b):
#    return a+ b, a * b
#
#
# num1 = int(input("Введи 1 число"))
# num2 = int(input("Введи 2 число"))
#
# s,d = my_sum(num1, num2)
#
# print("результат cуммы  = ", s )
# print("результат произведения  = ", d )



# var1 = 'Global'
#
#
# def foo():
#     global var2, var1
#     var1 = 'local'
#     var2 = 'local2'
#     print(var1)
#
#
# print(var1)
# foo()
# print(var2)

#def my_def(*args):
  #  print(args)
 #   return 'true'


#my_def( 1, 2, "true", 2.36)
#print(my_def())




# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
