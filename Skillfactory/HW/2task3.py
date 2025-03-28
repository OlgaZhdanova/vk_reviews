import numpy as np
# напишем функцию get_distance, которая на вход принимает два массива и возвращает значение Евклидова расстояния 
def get_distance(vec_1, vec_2):
    # с помощью np.linalg.norm высчитываем расстояние между двумя векторами
    distance = np.linalg.norm(vec_1 - vec_2)
    return distance
    
vec_1 = np.random.normal(0, 1, size = 100)
vec_2 = np.random.poisson(10, size = 100)

print(get_distance(vec_1, vec_2))

