def max_value(lst):
    return max(lst)

input_list = input ("Введите целочисленный список через пробел:")
list_of_numbers = list(map(int, input_list.split()))
print("Максимальное значение:", max_value(list_of_numbers))
