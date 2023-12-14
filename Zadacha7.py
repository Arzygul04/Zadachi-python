def reverse_string(input_string):
    return input_string[::-1]

def main():
    input_string = input("Введите строку: ")
    reversed_string = reverse_string(input_string)
    print("Инвертированное представление:", reversed_string)

if __name__ == "__main__":
    main()
