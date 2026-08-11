#Program 1
name = 'Shekha'
age = 21
cgpa = 8.9
is_student = True
print(name)
print(age)
print(cgpa)
print(is_student)

#Program 2 - Personal Information
name = input('Enter your name:')
age = int(input('Enter your age:'))
degree = input('Enter your degree:')
cgpa = float(input('Enter your CGPA:'))
print('You are a Student')

#Program 3 - Calculator
a = int (input('Enter first number:'))
b = int (input('Enter second number:'))
Addition = a + b
Subtraction = a - b
Multiplication = a * b
Division = a / b
FloorDivision = a // b
Remainder = a % b
Power = a ** b
print("Addition:", Addition)
print("Subtraction:", Subtraction)
print("Multiplication:", Multiplication)
print("Division:", Division)
print("FloorDivision:", FloorDivision)
print("Remainder:", Remainder)
print("Power:", Power)

#Program 4
name = input('Enter your name:')
birth = int(input('Enter your birth year:'))
current = int(input('Enter the current year:'))
age = current - birth
print(name,'is', age,'years old')