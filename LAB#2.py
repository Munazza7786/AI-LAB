Activity#01

myList1 = []
print("Enter objects of first list.......")
for i in range(5):
    val = input("Enter a value: ")
    n = int(val)
    myList1.append(n)

myList2 = []
print("Enter objects of second list.......")
for i in range(5):
    val = input("Enter a value: ")
    n = int(val)
    myList2.append(n)

myList3 = myList1 + myList2;
print(myList3)

Activity#02

def isPalindrome(word):
    temp = word[: : -1]
    if temp.capitalize() == word.capitalize():
        return True
    else:
        return False

print(isPalindrome("Deed"))

Activity#03

for indrow in range (3):
    c.append([])
    for indcol in range (3):
        c[indrow].append(0)
        for indaux in range (3):
            c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]

print(c)

Activity#04

def perimeter(listing):
    leng = len(listing)
    perimeter = 0;
    for i in range (0, leng-1):
        dist = (((listing[i][0] - listing[i+1][0])**2)+
                 ((listing[i][1] - listing[i+1][1])**2))**0.5
        perimeter = perimeter + dist
        perimeter = perimeter + (((listing[0][0] - listing[leng-1][0])**2)+
                            ((listing[0][1] - listing[leng-1][1])**2))**0.5

        return perimeter
L = [(1,3) , (2,7) , (3,9) , (-1,8)]
print(perimeter(L))
        
Activity#05

def symmDiff(a,b):
    e = set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e
set1 = {0,1,2,4,5}
set2 = {4,5,7,8,9}
print(symmDiff(set1,set2))

#verification using inbuilt function

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)

Activity#06

sample = {("Shoaib","Malik"):"0246585468445" , ("aib","li"): "02465854645",
          ("sib","ai"): "0246585468445",}
FirstName = input("Enter First Name>>>")
SecondName = input("Enter Second Name>>>")

searchTuple = (FirstName , SecondName)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("Name Not Found!!!!")


Task#01

list1=[]  
list2=[]  
num1=int(input("Enter number of elements for first list:"))
for i in range(1,num1+1):
    a=int(input("Enter element:"))
    list1.append(a)
num2=int(input("Enter number of elements for second list:"))
for i in range(1,num2+1):
    b=int(input("Enter element:"))
    list2.append(b)  
list3=list1+list2
list3.sort()
print("Sorted list is:",list3)  

Task#02

listNum=[]
num=int(input("How many numbers in list: "))
for n in range(num):
    numbers =int(input("Enter numbers: "))
    listNum.append(numbers)
print("Maximum elements in the list: ",max(listNum))
print("Minimum elements in the list: ",min(listNum))

Task#03

import math 
from math import *
x=float(input("enter x"))
h=0.001
m=(sin(x+h)-sin(x))/h
n=cos(x)
m=math.ceil(m*100)/100
n=math.ceil(n*100)/100
if(math.isclose(m,n)):
    print("Equal")
else:
    print("Not Equal")
print(m)
print(n)

Task#04

birthday={("Mirha"):"21 September 2021",("Munazza"):"28 March 2002",("Ajaib"):"1 September 1978"}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for key, value in birthday.items():
    print(key)
M =input("Who's birthday do you want to look up!!!!!")
M=M.capitalize()
if M in birthday:
    print(birthday[M])
else :
    print("NO Result found<><>")


Task#05

smaple={"Name":"Murtaza Ahmed","Age":"22","Salary":"400000","Country":"Italy"}
keys=["Name","Country"]
dic2=dict()
for i in keys:
    dic2.update({i:smaple[i]})
print(dic2)
