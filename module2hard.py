# Получение списка паролей
print('Получаем комбинации ключей в зависимости от параметра "number":')
# Создаем список для комбинаций ключей
mean_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def get_pairs(number):
    mean_pairs = []  #Создаем пустой список
    for a in range(len(mean_2)):  # Выбираем первый элемент списка
        for b in range(a + 1, len(mean_2)):  # Выбираем последующий элемент списка
            if number % (mean_2[a] + mean_2[b]) == 0:  # Если делится без остатка то
                mean_pairs.append(f" {mean_2[a]}{'+'}{mean_2[b]}")  # добавляем эту пару в список
    combo = ''.join(mean_pairs)  # Объединяем элементы списка в строку
    #print(combo)
    return combo


# get_pairs(9)
# get_pairs(18)
for number in range(3, 21):  # для get_pairs задаем параметр number
    print(f"{number} * {get_pairs(number)}")  # Выводим на печать
