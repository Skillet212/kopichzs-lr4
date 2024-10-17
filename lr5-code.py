import numpy as np

#Функция для подсчета суммы элементов на нечетных позициях в строке.
def sum_of_odds_in_row(row):
    return np.sum(row[1::2])  # Суммируем элементы на нечетных позициях

#Функция для подсчета количества строк с положительной суммой элементов на нечетных позициях.
def count_positive_odd_sums(matrix):
    count = 0
    row_numbers = []
    
    for i, row in enumerate(matrix):
        odd_sum = sum_of_odds_in_row(row)
        if odd_sum > 0:
            count += 1
            row_numbers.append(i + 1)  # Номера строк начинаются с 1
    
    return count, row_numbers

#Функция для генерации случайного двумерного массива с использованием numpy.
def generate_random_matrix(rows, cols, value_range):
    return np.random.randint(value_range[0], value_range[1] + 1, size=(rows, cols))

# Генерация случайных массивов размером до 10x10
rows1, cols1 = np.random.randint(1, 11), np.random.randint(1, 11)
rows2, cols2 = np.random.randint(1, 11), np.random.randint(1, 11)

matrix1 = generate_random_matrix(rows1, cols1, (-10, 10))
matrix2 = generate_random_matrix(rows2, cols2, (-10, 10))

# Подсчет строк с положительной суммой для каждого массива
count1, row_numbers1 = count_positive_odd_sums(matrix1)
count2, row_numbers2 = count_positive_odd_sums(matrix2)

# Вывод результатов
print("Первый массив:")
print(matrix1)

if count1 > 0:
    print(f"\nВ первом массиве количество строк с положительной суммой на нечетных местах: {count1}")
    print(f"Номера строк: {row_numbers1}")
else:
    print("В первом массиве нет строк с положительной суммой на нечетных местах.")

print("\nВторой массив:")
print(matrix2)

if count2 > 0:
    print(f"\nВо втором массиве количество строк с положительной суммой на нечетных местах: {count2}")
    print(f"Номера строк: {row_numbers2}")
else:
    print("Во втором массиве нет строк с положительной суммой на нечетных местах.")