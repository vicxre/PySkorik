#Даны строки S, S1 и S2. Заменить в строке S последнее вхождение строки S1 на строку
#S2.


s = 'салют мир! салют всем!'
s1 = 'салют всем'
s2 = 'добро пожаловать'


def zamena(s , s1, s2):

    last_pos = s.rfind(s)

    if last_pos != -1:
        result = s[:last_pos] + s2 + s[last_pos + len(s1):]

    else:
        result = s

    return result


print(zamena(s, s1, s2))








