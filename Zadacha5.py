def find_index(input_list, val):
    if val in input_list:
        return input_list.index(val)
    else:
        return None

def main():
    input_numbers = input("Введите список чисел, разделенных пробелами: ")
    number_list = list(map(int, input_numbers.split()))
    search_value = int(input("Введите значение для поиска: "))
    result_index = find_index(number_list, search_value)
    print("Индекс", search_value, "в списке:", result_index)

if __name__ == "__main__":
    main()
