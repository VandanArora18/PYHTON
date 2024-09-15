
subjects = {"python","java","C++","pyhton","javascript","java","pyhton","java","C++","C"}
print(" No of classrooms needed:",len(subjects))


dict = {}
Subject1 = input("write the name of the of subject 1:",)
Subject2 = input("write the name of the of subject 2:",)
Subject3 = input("write the name of the of subject 3:",)
dict[Subject1]=45
dict[Subject2]=65
dict[Subject3]=75
print(dict)





store = set()
store.add(9)
store.add("9.0")
print(store)



line1 = "Twinkle, twinkle, little star,"
line2 = "How I wonder what you are!"
line3 = "Up above the world so high,"
line4 = "Like a diamond in the sky."
print(f"\t{line1}\n\tline2\n\tline3\n\tline1\n\tline4")#format
print("\n\t"+line1+"\n\t"+line2+"\n\t"+line3+"\n\t"+line1+"\n\t"+line4)




a=input("enter your name:")
b=input("enter your surname:")
print(b+"\t"+a)




a= int(input("enter the radius of circle:"))
b= (3.14*a**2)
print(b)




color_list=["Red", "Green", "White", "Black"]
print(color_list[0],"\n",color_list[-1])


#qus5
n = int(5)
b= n+n*n+n*n*n*n
print(b)





celcious = int(input("enter the value in celcious:"))
fahrehiet = celcious*9/5+32
print("fa",fahrehiet)


a =int(input("enter the first number:"))
b =int(input("enter the second number:"))
a,b = b,a
print(a,b)
increment = 8
c = increment+a
print(c)



N = int(input("enter a positive integer"))
b = N*(N+1)*(2*N+1)/6
print(b)





a=  (1,2,3,4,5,0)
print(a[1:6])

Dict = {"name":"rahul",
        "age":34,
    }
Dict.update({"Marks":8})
print(Dict.keys())



a = {1,24,5,5,}
a.add(10)
a.pop()
a.clear()
print(a)



a= int(input("enter a number:"))
if(a%2==0):
    print("The number is even")
elif():
 print("The number is odd ")










angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))


if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle")
else:
    print("The angles cannot form a triangle")





celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")





import math
x1, y1 = map(float, input("Enter coordinates  (x1, y1): ").split())
x2, y2 = map(float, input("Enter coordinates  (x2, y2): ").split())
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f" Euclidean distance between the points is: {d}")




a1 = float(input("Enter  first angle: "))
a2 = float(input("Enter second angle: "))
a3 = float(input("Enter third angle: "))
if a1 + a2 + a3 == 180:
    print("angles can form a triangle")
else:
    print(" angles cannot form a triangle")
