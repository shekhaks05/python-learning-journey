#Reverse a number.
num = int(input('Enter a number:'))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print ('Reversed number:', rev) 

#Check whether a number is a palindrome.
num = int(input('Enter a number:'))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print ('Palindrome')
else:
    print('Not a Palindrome')

#Check whether a number is prime.
num = int(input('Enter a number:'))
if num < 2:
    print('Not a prime number')
else:
    is_prime = True
    for i in range(2,num):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
        print('Prime number')
    else:
        print('Not a prime number')

#Print all prime numbers between 1 and 100.
for num in range(2,101):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#Simple calculator using if/elif/else.
num1 = float(input('Enter first number:'))
operator = input('Enter operator:')
num2 = float(input('Enter second number:'))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1/ num2
    else:
        result = 'Cannot divide by zero' 
else:
    result = 'Invalid operator'
print('Result:', result)