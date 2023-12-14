from typing import Dict

def find_key_by_value(my_map: Dict[int, str], value: str) -> int:
    for key, val in my_map.items():
        if val == value:
            return key
    return None

my_map = n = int(input("Введите количество элементов в Map: "))
for i in range(n):
    key = int(input("Введите ключ: "))
    value = input("Введите значение: ")
    my_map[key] = value

search_value = input("Введите строку для поиска: ")
result = find_key_by_value(my_map, search_value)
print(result)
