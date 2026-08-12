#Calculate the Area of a Rectangle.
length = float(input('Enter the length :'))
breadth = float (input('Enter the breadth:'))
area = length * breadth
print('The area of the rectangle is :', area, 'cm²')

#Calculate the total and average of 3 numbers.
a = float(input('Enter the first number:'))
b = float(input('Enter the second number:'))
c = float(input('Enter the third number:'))
total = a + b + c
average = total / 3
print ('The total of 3 numbers is', total)
print ('The average of 3 numbers is', average)

#Check whether a number is even or odd.
number = int(input('Enter the number:'))
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

#Check whether someone is eligible to vote based on age.
age = int(input('Enter your age:'))
if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

#Check whether two numbers are equal.
a = int(input('Enter the first number:'))
b = int(input('Enter the second number:')) 
if a==b:
    print('Both numbers are same')
else:
    print('Numbers are not equal')

#Calculate the remainder when 57 is divide by 8.
remainder = 57 % 8
print('Remainder:', remainder)

# Calculate 2 raised to the power 5.
result = 2 ** 5
print('Answer:', result)

#Experiment with +=, -= and *=
a = 10
b = 5
a += b
print ('After += :', a)
a -= b
print ('After -= :', a)
a *= b
print ('After *= :', a)

#WAP that takes a person's marks in 3 subjects and prints total, average, passed : True or false
marks1 = float(input('Enter marks for subject 1:'))
marks2 = float(input('Enter marks for subject 2:'))
marks3 = float(input('Enter marks for subject 3:'))
total = marks1 + marks2 + marks3
average = total / 3
passed = marks1 >= 40 and marks2 >= 40 and marks3>= 40
print('Total :', total)
print('Average :', average)
print('Passed :', passed)