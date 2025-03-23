#string импортирован объект ascii_letters,в котором содержатся только буквы английского алфавита




from string import ascii_letters

letters = 'hыtφтrцзqπ'
# Разграничиваем буквы на английские и не английские


is_eng = [f'{letter}-ДА' if letter in ascii_letters else f'{letter}-НЕТ' for
letter in letters]

print(is_eng)
