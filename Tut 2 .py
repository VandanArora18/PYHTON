#qus1
L = [11, 12, 13, 14]
L.extend([50, 60])
L.remove(11)
L.remove(13)
L.sort()
L.sort(reverse=True)


if 13 in L:
    print("13 is in  list")
else:
    print("13 is not in list")

 
num_elements = len(L)
print("Number of elements:", num_elements)


total_sum = sum(L)
print("Sum of all elements:", total_sum)

 
Sum_odd = sum(x for x in L if x % 2 != 0)
print("Sum of odd numbers:", Sum_odd)

 
Sum_even = sum(x for x in L if x % 2 == 0)
print("Sum of even numbers:", Sum_even)

 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_sum = sum(x for x in L if is_prime(x))
print("Sum of prime numbers:", prime_sum)

 
L.clear()
del L






#qus 2
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total



#qus 3
def multiply_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product






#qus 5
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}


D[8] = 8.8

 
del D[2]


if 6 in D:
    print("Key 6 is present.")
else:
    print("Key 6 is not present.")


count = len(D)
print("Number of elements:", count)


sum_values = sum(D.values())
print("Sum of values:", sum_values)


D[3] = 7.1
D.clear()




#qus 6
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}


S1.add(55)
S1.add(66)

 
S1.remove(10)
S1.remove(30)


if 40 in S1:
    print("40 is present in S1.")
else:
    print("40 is not present in S1.")

 
union_set = S1 | S2


intersection_set = S1 & S2


difference_set = S1 - S2

#qus 7
import random

 
for _ in range(100):
    length = random.randint(6, 8)
    string = ''.join(random.choices(string.ascii_letters, k=length))
    print(string)


def is_prime(num):
 

 for num in range(600, 801):
    if is_prime(num):
        print(num)

for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num)


#qus 8
exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date
print("Exam start date:", day, "/", month, "/", year) 

#qus 9
numbers = [1, 5, 10, 15, 20, 23, 25]
for number in numbers:
    if number % 5 == 0:
        print(number)


#qus10
def is_even(number):
    return number % 2 == 0

num = 10
if is_even(num):
    print(num, "is even.")
else:
    print(num, "is odd.")

#qus11
def count_emma(string):
    count = 0
    for i in range(len(string) - len("Emma") + 1):
        if string[i:i+len("Emma")] == "Emma":
            count += 1
    return count

text = "Emma is girl. Emma likes to play ."
result = count_emma(text)
print("'Emma' appears", result, "times ")


#qus 12
def create_new_list(list1, list2):
    new_list = []
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
new_list = create_new_list(list1, list2)
print("New list:", new_list)