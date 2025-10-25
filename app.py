students_count = 1000
print(students_count)

x = 10
y = 20
result = x+y
print(result)


z = 20
r = 30
print(z+r)

a = 5
b = 4
print(a*b)

Student = "John"
print(len(Student))
print(Student[0:2])
print(Student[:])

First = "Sai swetha"
Last = "Kondamadugula"
Full = First + " " + Last
print(Full)

course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.title())
print("Python" in course)

print(10 + 3)
print(10 - 3)
print(10 % 3)
print(10//3)
print(abs(-7))
print(round(3.7))
print(2 ** 3)

x = input("x: ")
y = int(x)+1
print(f"x:{x}, y:{y}")

print(bool("false"))

temperature = 10
if temperature > 25:
    print("It's a hot day")
    print("Drink plenty of water")
print("Done")


for number in range(3):
    print("Hello World")


for number in range(3):
    print("Hello World", number)

for number in range(1, 10, 2):
    print("Hello World", number, number * ".")


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet_user("Sai", "Swetha")
