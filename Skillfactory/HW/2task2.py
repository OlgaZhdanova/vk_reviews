import numpy as np
data = np.array([ # исходные данные с задачи2 ДЗ1
    [25, -19, 35, 90, 73],
    [14.86452745, -26.8915466, -4.42219305, 6.3526264, 7.88297253],
    [0, 0, 1, 0, 1],
    [837, 302, 790, 271, 796],
    [49.97, 49.94, 51.37, 50.97, 51.29]
])
# находим минимальный элемент в списке
data_mn = np.min(data, axis=1)
# преобразуем массив с минимальными значениями в размерность массива data
data_mn_reshape = data_mn.reshape((5,1))
# находим максимальный элемент в списке
data_mx = np.max(data, axis=1)
# преобразуем массив с максимальными значениями в размерность массива data
data_mx_reshape = data_mx.reshape((5,1))
# формула по условию: x_scaled = x - xmin / xmax - xmin
# вычисляем числитель
numerator = np.subtract(data, data_mn_reshape)
# вычисляем знаменатель
denominator = np.subtract(data_mx_reshape, data_mn_reshape)
# с помощью np.divide делим числитель на знаменатель
x_scaled = np.divide(numerator, denominator)

print(x_scaled)