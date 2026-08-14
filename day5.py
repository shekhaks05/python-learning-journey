#Print numbers from 1 to 10 using for.
for i in range (1,11):
    print(i)

 #Print numbers from 10 to 1 using for.
for i in range (10,0,-1):
    print(i)

# Print even numbers from 1 to 20.
i = 2
while i <= 20:
    print(i)
    i += 2

#Print odd numbers from 1 to 20.
i = 1
while i <= 20:
    print(i)
    i += 2

#Print the multiplication table of a number.
num = int(input('Enter a number:'))
print('Multipliaction table of', num)
for i in range (1,11):
    print(f"{num}x{i} = {num * i}")

#Find the sum of numbers from 1 to 100.
total = 0
for i in range(1,101):
    total = total + i
print(total)

#Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i*i)

#Count backwards from 10 to 1 using while.
i = 10
while i >= 1:
    print(i)
    i = i - 1

#Print Python 5 times
for i in range(5):
    print('Python')