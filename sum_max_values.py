import pandas as pd

# Функция для чтения данных из CSV и нахождения суммы наибольших значений в каждой строке
def sum_max_values(csv_file):
    # Чтение CSV-файла в DataFrame
    df = pd.read_csv(csv_file)
    
    # Список для хранения максимальных значений
    max_values = []
    
    # Обход всех строк, кроме последней
    for i in range(len(df) - 1):
        row = df.iloc[i]
        max_value = row.max()
        
        # Проверка, в какой колонке находится максимальное значение
        if max_value == row.iloc[0]:
            # Если максимальное значение в первой колонке, записываем значение первой колонки из следующей строки
            max_values.append(df.iloc[i + 1, 0])
        else:
            # Иначе записываем максимальное значение
            max_values.append(max_value * 0.95)
    
    # Суммирование всех записанных значений
    total_sum = sum(max_values)
    
    return total_sum


