import pandas as pd

# Функция для чтения данных из CSV и нахождения суммы наибольших значений в каждой строке
def sum_max_values_percent(csv_file):
    # Чтение CSV-файла в DataFrame
    df = pd.read_csv(csv_file)
    
    # Список для хранения значений
    values = []
    
    # Обход всех строк, кроме последней
    for i in range(len(df) - 1):
        row = df.iloc[i]
        max_value = row.max()
        first_col_value = row.iloc[0]
        
        # Проверка, в какой колонке находится максимальное значение
        if max_value == row.iloc[0]:
            # Если максимальное значение в первой колонке, записываем значение первой колонки из следующей строки
            values.append(df.iloc[i + 1, 0])
        else:
            # Проверка отклонения на 5%
            if max_value <= 1.05 * first_col_value:
                # Если максимальное значение отклоняется не более чем на 5%, берем значение из следующей строки первой колонки
                values.append(df.iloc[i + 1, 0])
            else:
                # Иначе записываем максимальное значение
                values.append(max_value * 0.95)
    
    # Суммирование всех записанных значений
    total_sum = sum(values)
    
    return total_sum

