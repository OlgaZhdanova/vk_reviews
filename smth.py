import numpy as np
# импортируем MixMaxScaler из библиотеки scikit-learn для масштабирования набора данных таким образом, чтобы значения находились между нулем и единицей
from sklearn.preprocessing import MinMaxScaler
# напишем функцию get_result, которая на вход принимает массив и возвращает массив с измененными по формуле данными
def get_result(data):
    # воспользуемся методом stack
    stacked_data = np.stack(data, axis=1)
    # 
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(stacked_data)
    return scaled_data.transpose()
'''data = np.array([ #исходные данные
    [25, -19, 35, 90, 73],
    [14.86452745, -26.8915466, -4.42219305, 6.3526264, 7.88297253],
    [0, 0, 1, 0, 1],
    [837, 302, 790, 271, 796],
    [49.97, 49.94, 51.37, 50.97, 51.29]
])'''
simulated_data = np.random.uniform(-1000, 1000, (10, 10000))

print(get_result(data = simulated_data))

#a = simulated_data.min(axis = 1)
#b = simulated_data.max(axis = 1)