from sum_max_values import sum_max_values 
from sum_max_values_percent import sum_max_values_percent 

if __name__ == "__main__":
    # csv_file = 'random_numbers_10000.csv'  
    # csv_file = 'random_numbers_3000.csv' 
    csv_file = 'random_numbers_300.csv' 
    result = sum_max_values(csv_file)
    result_p = sum_max_values_percent(csv_file)
    print(f'Без проверки: {result}, с погрешностью 5%: {result_p}')