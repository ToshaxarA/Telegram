# Задание 1
"""Создайте вручную список из 15 элементов (название городов, музыки,
машины). Сделайте срез от 2-го индекса до 7-го"""

# list1= ["Майами", "Сан Тропе", "Константинополь", "Нальчик", "Квебек", "Анталия", "Иркутск",
#        "Мурманск", "Сеул", "Веллингтон", "Купянск", "Рыбинск", "Сан Франциско", "Канберра", "Мирный"]
# print(list1[2:7])

# Задание 2
# Создайте вручную список из чисел и выведите их в обратном порядке

lst2 = [12, 34, 6, 77, 544, 345, 77, 8, 3, 22]
# print(lst2[::-1])

# Задание 3 
# Найдите наименьший элемент в списке из задания 2

# print(min(lst2))       #Наименьший элемент 3

# Задание 4
# Удалите все элементы из списка, созданного в задании 2
# del lst2[:]
# print(lst2)

# Задание 5 
# Найдите сумму элементов списка из задания 2

# print(sum(lst2))

# Задание 6
# Найдите среднее арифметическое элементов списка из задания 2 

# import statistics
# print("Среднее арифметическое элементов списка =",statistics.mean(lst2))   # Среднее арифметическое элементов списка = 112.8

# Задание 7
"""Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189,
190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206,
207, 208, 209, 210, 211, 212, 213, 214, 215,
216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232,
233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249,
250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266,
267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283,
284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110,
111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127,
128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
145, 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277,
278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294,
295, 296, 297, 298, 299, 110] 
Выясните сколько раз цифра 110 встречается в списке """

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
# 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
# 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
# 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
# 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
# 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
# 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
# 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
# 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
# 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189,
# 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206,
# 207, 208, 209, 210, 211, 212, 213, 214, 215,
# 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232,
# 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249,
# 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266,
# 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283,
# 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110,
# 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127,
# 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
# 145, 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
# 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277,
# 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294,
# 295, 296, 297, 298, 299, 110]

# print(numbers.count(110))   # цифра 110 встречается 3 раза

# Дополнительное задание 8
# Даны два списка, удалите все элементы первого списка из второго, то есть
# дубликаты.

a = [1, 3, 4, 5]
b = [4, 5, 6, 7]
 
# c = [];
# for i in range(len(b)):     # Перебираю второй список
#     if b[i] in a:           # Если элемент второго списка есть в первом
#         c.append(b[i])      # Записываю этот элемент в третий список
        
# for z in range(len(c)):     # Перебираю третий список
#     b.remove(c[z])          # Удаляю из второго списка все значения, которые есть в третьем
           
# print(b)
    
# Дополнительное задание 9
# Создайте плейлист из 10 любимых песен, поменяйте 4-й с 8-м и выведите на
# экран весь плейлист

# def out_red(text):
#     print("\033[31m {}" .format(text))
# def out_blue(text):
#     print("\033[34m {}" .format(text))

# playlist = ["Мальчик на девятке", "Женская сборная по баскетболу", "Я свободен", "Гимн обречённых",
#             "Seven Nation Army", "Якутяночка", "Я так соскучился", "Батарейка", "Арабская ночь", "Чёрный плащ"]

# out_red("       Мой изначальный плейлист      ")
# for i in playlist:
#     print(i)

# out_blue("       Мой плейлист с перестановкой      ")
# playlist[3],playlist[7] = playlist[7],playlist[3]
# for j in playlist:
#     print(j)