from typing import List

def find_product_of_elements(nums:List[int])->int:
    product = 1
    for num in nums:
        product *= num
    return product

input_str = input("Введите целочисленный список через пробел:")
nums = list(map(int,input_str.split()))

result = find_product_of_elements(nums)
print(result)
