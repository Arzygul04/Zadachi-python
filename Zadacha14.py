class Student:
    def init(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


# Создание экземпляров класса Student
student1 = Student("John", 20, "11B")
student2 = Student("Alice", 19, "12C")
student3 = Student("Bob", 21, "9A")
student4 = Student()
student5 = Student()

# Изменение данных атрибутов установленных по умолчанию
student4.setNameAge("Kate", 22)
student5.setGroupNumber("8B")

# Вывод данных о студентах
print("Student 1:", student1.getName(), student1.getAge(), student1.getGroupNumber())
print("Student 2:", student2.getName(), student2.getAge(), student2.getGroupNumber())
print("Student 3:", student3.getName(), student3.getAge(), student3.getGroupNumber())
print("Student 4:", student4.getName(), student4.getAge(), student4.getGroupNumber())
print("Student 5:", student5.getName(), student5.getAge(), student5.getGroupNumber())
