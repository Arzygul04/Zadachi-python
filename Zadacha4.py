def create_number_list():
    input_numbers = input("Введите список чисел, разделенных пробелами: ")
    number_list = list(map(int, input_numbers.split()))
    return number_list

result_list = create_number_list()
print("Итоговый список:", result_list)
