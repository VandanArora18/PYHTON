


#qus 1
def calculate_difference(number): 
    
    difference = number - 17
    if number > 17:
        difference *= 2
    return difference
result = calculate_difference(20)
print(result)


#qus 2
def is_within_range(number):
   
    return (100 <= number <= 1000) or (number == 2000)


result = is_within_range(500)
print(result) 




#qus3
def reverse_string(s):
    

    return s[::-1]


result = reverse_string("hello")
print(result)  



#qus 4
def count_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


result = count_letters("Python, Programming")
print(result) 



#qus 5
def remove_duplicates(lst):
    return list(set(lst))

result = remove_duplicates([1, 2, 3, 2, 4, 1])
print(result)  




#qus 6
def print_even_numbers(lst):

    for num in lst:
        if num % 2 == 0:
            print(num)

print_even_numbers([2,3,4,6,2,3,45,5,7])



#qus7
def outer_function():
    def inner_function():
        print("This is the inner function.")

    inner_function()


outer_function()



#qus 8
def student(name, age, grade):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")


student("Alice", 18, "10th")






#qus9
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")


student1 = Student(123, "Rahul")
student1.student_class = "10th"
student1.display_attributes()






#qus10
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(123, "xyz")
student2 = Student(456, "ABC")

print(f"Student 1: ID={student1.student_id}, Name={student1.student_name}")
print(f"Student 2: ID={student2.student_id}, Name={student2.student_name}")



#qus11
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print(f"Area: {circle.calculate_area()}")
print(f"Perimeter: {circle.calculate_perimeter()}")



#Qus 12
class StringProcessor:
    def string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())


processor = StringProcessor()
processor.string()
processor.print_string()