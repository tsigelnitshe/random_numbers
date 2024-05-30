import pandas as pd
import random

# Функция для чтения данных из CSV и нахождения суммы по усложненному алгоритму
def sum_max_values_dsp(csv_file):
    df = pd.read_csv(csv_file)
    
    # Список для хранения значений
    values = []
    
    # Списки для хранения значений bad_traffic для каждой колонки
    bad_traffic_col2 = []
    bad_traffic_col3 = []
    bad_traffic_col4 = []
    
    for i in range(len(df) - 1):
        row = df.iloc[i]
        max_value = row.max()
        first_col_value = row.iloc[0]
        
        # Генерация случайных значений bad_traffic для каждой колонки
        bad_traffic_2 = random.uniform(0, 0.05)
        bad_traffic_3 = random.uniform(0, 0.10)
        bad_traffic_4 = random.uniform(0.05, 0.10)
        
        # Сохранение значений bad_traffic
        bad_traffic_col2.append(bad_traffic_2)
        bad_traffic_col3.append(bad_traffic_3)
        bad_traffic_col4.append(bad_traffic_4)
        
        # Проверка, в какой колонке находится максимальное значение
        if max_value == first_col_value:
            values.append(df.iloc[i + 1, 0])
        else:
            # Проверка отклонения с учетом случайных значений bad_traffic
            if max_value == row.iloc[1] and max_value <= (1 + bad_traffic_2) * first_col_value:
                values.append(df.iloc[i + 1, 0])
            elif max_value == row.iloc[2] and max_value <= (1 + bad_traffic_3) * first_col_value:
                values.append(df.iloc[i + 1, 0])
            elif max_value == row.iloc[3] and max_value <= (1 + bad_traffic_4) * first_col_value:
                values.append(df.iloc[i + 1, 0])
            else:
                # Иначе записываем максимальное значение за вычетом соответствующего bad_traffic
                if max_value == row.iloc[1]:
                    values.append(max_value * (1 - bad_traffic_2))
                elif max_value == row.iloc[2]:
                    values.append(max_value * (1 - bad_traffic_3))
                elif max_value == row.iloc[3]:
                    values.append(max_value * (1 - bad_traffic_4))
    
    # Суммирование всех записанных значений
    total_sum = round(sum(values), 2)
    
    # Подсчет среднего значения bad_traffic для каждой колонки
    avg_bad_traffic_col2 = round(sum(bad_traffic_col2) / len(bad_traffic_col2), 4)
    avg_bad_traffic_col3 = round(sum(bad_traffic_col3) / len(bad_traffic_col3), 4)
    avg_bad_traffic_col4 = round(sum(bad_traffic_col4) / len(bad_traffic_col4), 4)

    return total_sum, avg_bad_traffic_col2, avg_bad_traffic_col3, avg_bad_traffic_col4
