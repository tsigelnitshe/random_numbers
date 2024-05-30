from sum_max_values import sum_max_values 
from sum_max_values_percent import sum_max_values_percent 
from sum_max_values_dsp import sum_max_values_dsp 

if __name__ == "__main__":
    # csv_file = 'random_numbers_10000.csv'  
    csv_file = 'random_numbers_3000.csv' 
    # csv_file = 'random_numbers_300.csv' 
    result = sum_max_values(csv_file)
    result_p = sum_max_values_percent(csv_file)
    result_dsp, avg_traffic_col2, avg_traffic_col3, avg_traffic_col4 = sum_max_values_dsp(csv_file)
    avg_bad_traffic = (avg_traffic_col2 + avg_traffic_col3 + avg_traffic_col4)/3
    print(f'Без проверки: {result}, с погрешностью 5%: {result_p}, случайный bad_traffic для dsp {result_dsp}')
    print(f'Среднее значение bad_traffic для dsp1: {avg_traffic_col2}')
    print(f'Среднее значение bad_traffic для dsp2: {avg_traffic_col3}')
    print(f'Среднее значение bad_traffic для dsp3: {avg_traffic_col4}')
    print(f'Среднее значение bad_traffic: {avg_bad_traffic}')