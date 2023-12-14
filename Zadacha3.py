def sum_of_elements(lst1, lst2):
    return sum(lst1) + sum(lst2)

input_list1 = input("Введите первый список целых чисел, разделенных пробелами: ")
input_list2 = input("Введите второй список целых чисел, разделенных пробелами: ")

list_of_numbers1 = list(map(int, input_list1.split()))
list_of_numbers2 = list(map(int, input_list2.split()))

print("Сумма элементов:", sum_of_elements(list_of_numbers1, list_of_numbers2))
