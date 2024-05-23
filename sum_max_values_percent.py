import pandas as pd
from vars import bad_traffic

def sum_max_values_percent(csv_file):
    
    df = pd.read_csv(csv_file)
    
    # Список для хранения значений
    values = []
    
    for i in range(len(df) - 1):
        
        row = df.iloc[i]
        max_value = row.max()
        first_col_value = row.iloc[0]
        
        # Проверка, в какой колонке находится максимальное значение
        if max_value == first_col_value:
            values.append(df.iloc[i + 1, 0])
        else:
            # Проверка отклонения 
            if max_value <= (1+bad_traffic) * first_col_value:
                # Если максимальное значение отклоняется не более чем на bad_traffic, берем значение из следующей строки первой колонки
                values.append(df.iloc[i + 1, 0])
            else:
                # Иначе записываем максимальное значение за вычетом bad_traffic
                values.append(max_value * (1-bad_traffic))
    
    # Суммирование всех записанных значений
    
    total_sum = round(sum(values), 2)
    
    return total_sum

