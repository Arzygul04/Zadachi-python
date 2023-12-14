def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

print(check_anagram(word1, word2))
