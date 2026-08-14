#Check whether a number is positive, negative, or zero.
num = float(input('Enter a number:'))
if num > 0:
    print('The number', num, 'is positive')
elif num < 0:
    print('The number', num, 'is negative')
else:
    print ('The number is zero')

#Check whether a person is eligible to vote.
age = int(input('Enter your age:'))
if age >= 18:
    print('You are eligible to vote')
else :
    print('You are not eligible to vote')

#Check whether a number is even or odd.
num = int(input('Enter a number:'))
if num % 2 == 0:
    print('Even number')
else:
    print('Odd number')

#Take marks and print: 90-100 A+, 80-89 A, 70-79 B, 60-69 C, Below 60 Fail.
marks = int(input('Enter the marks:'))
if marks >= 90 and marks <=100:
    print('A+')
elif marks >= 80 :
    print('A')
elif marks >= 70:
    print('B')
elif marks >= 60:
    print('C')
else:
    print('Fail')

#Take two numbers and print which one is larger.
num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:')) 
if num1 > num2:
    print(num1,'is larger')
else:
    print(num2,'is larger')