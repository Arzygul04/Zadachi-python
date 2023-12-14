def check_bit_set(A, B):
    return (A >> B) & 1 == 1

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print(check_bit_set(A, B))
