Activity#1
n = input("Enter a number")
if int(n)%2 == 0:
    print("The given number is an even number")
else:
    print("The given number is an odd number")
    
Activity#2
sum = 0
s = input("Enter an integer value...")
n = int(s)
while n!=0:
    sum = sum+n
    s = input("Enter an integer value...")
    n = int(s)
print("Sum of given values is ",sum)

Activity#3

isPrime = True
i = 2
n = int(input("Enter a number"))
while i<n:
    remainder = n%i
    if remainder == 0:
        isPrime = False
        break
    else:
        i = i+1

if isPrime :
    print("Number is prime")
else:
    print("Number is not prime")

Activity#4
summ = 0
i =0
while i<=4:
    s=input("Enter a number")
    n = int(s)
    summ = summ+n
    i = i+1

Activity#5

summation = 0
i = 1
while i<=10:
    summation = summation+i
    i = i+1
print("Sum is>>>>",summation)

Activity#6
name = input("What is your name?")
print("Hello!!!!" +name)
job = input("What is your job?")
print("My job is>>>>" +job)
num = input("Give me a number?")
print("You said: " +str(num))

Activity#7

import random
minimum = 1
maximum = 9
number = random.randint(minimum, maximum)
guess = None
another = None
Try = 0
running = True
print ("Alright...")
guess =  input("What is your lucky number? ")

if int(guess) < number:
    print ("Wrong, too low.")
elif int(guess) > number:
    print ("Wrong, too high.")
elif guess.lower() == "exit":
    print ("Better luck next time.")
elif int(guess) == number:
    print ("Yes, that's the one, %s." % str(number))
if Try < 2:
    print ("Impressive, only %s tries." % str(Try))
elif Try > 2 and TRY < 10:
    print ("Pretty good, %s tries." % str(Try))
else:
    print ("Bad, %s tries." % str(Try))
running = False
Try += 1

Task#1

try:
    n = int(input("Enter a number....."))
    reversed = 0
    while(n!=0):
        r = int(n%10)
        reversed = reversed*10+r
        n=int(n/10)
        print(reversed)

except ValueError:
    print("Given input is not a number!!!!!!")

Task#2

list = [345,678,4566,777,7898]
print("The original list is>>>>", list)
odd_sum = 0
even_sum = 0
for sub in list:
    for ele in str(sub):
        if int(ele)%2 == 0:
            even_sum += int(ele)
        else:
            odd_sum +=int(ele)

print("Odd digit Sum >>>> " + str(odd_sum))
print("Even digit Sum >>>> " + str(even_sum))


Task#3

nterms = int(input("Number of terms??"))
n1 = 0
n2 = 1
count = 0

if nterms <=0:
    print("Enter the positive integers.....")
elif nterms == 1:
    print("Fibonacci sequence upto" , nterms,":")
    print(n1)

else:
    print("Fibonacci sequence : ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


Task#4

print("Enter the marks obtained in 5 subjects")
subject_one = int(input())
subject_two = int(input())
subject_three = int(input())
subject_four = int(input())
subject_five = int(input())
Total = subject_one + subject_two + subject_three + subject_four + subject_five
average = Total/5

if average>=91 and average>=100:
    print("Got Grade A")
elif average>=81 and average>=90:
    print("Got Grade B")
elif average>=71 and average>=80:
    print("Got Grade C")
elif average>=61 and average>=70:
    print("Got Grade D")
elif average>=50 and average>=60:
    print("Got Grade E")
elif average < 50:
    print("You are fail!!!!")
else:
    print("Invalid")

Task#5

num = int(input("Enter a number>>>>> "))
fac = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The fatorial of 0 is 1")
else:
    for i in range (1,num + 1):
        fac = fac*i
        print("The Factorial of ",num, "is" , fac)
