# -*- coding: utf-8 -*-
"""if else.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KvWS0rKBTt-57GKDiMHNLSqVMyTmSfBP
"""

num=int(input("Enter the Number"))
if(num%2==0):
  print("EVEN")
else:
  print("ODD")

a=int(input("Enter the First number"))
b=int(input("Enter the Second number"))
c=int(input("Enter the third number"))
if(a>b and a>c):
  print("a is greatest with value ",a)
elif(b>a and b>c):
  print("b is greatest with value ",b)
else:
  print("c is greatest with value ",c)

year=int(input("Enter the YEAR"))
if(year%400==0):
  if(year%100==0):
    if(year%4==0):
      print("LEAP YEAR")
    else:
      print("Not a LEAP YEAR")
  else:
     print("Not a LEAP YEAR")
else:
   print("Not a LEAP YEAR")

percentage=int(input("ENter the percentage"))
if(percentage>=90):
  print("GRADE A")
elif(percentage>=80):
  print("GRADE B")
elif(percentage>=70):
  print("GRADE C")
elif(percentage>=60):
  print("GRADE D")
else:
  print("GRADE F")

char=input("Enter the character ")
if(char=='a'):
  print("VOWEL")
elif(char=='e'):
  print("VOWEL")
elif(char=='i'):
  print("VOWEL")
elif(char=='o'):
  print("VOWEL")
elif(char=='u'):
  print("VOWEL")
else:
  print("CONSONENT")

a=int(input("Enter the first number "))
b=int(input("Enter the Second number"))
symbol=input("Enter the symbol ")
if(symbol=="+"):
  ans=a+b
  print("the ans is ",ans)
elif(symbol=="-"):
  ans=a-b
  print("the ans is ",ans)
elif(symbol=="*"):
  ans=a*b
  print("the ans is ",ans)
elif(symbol=="/"):
  ans=a/b
  print("the ans is ",ans)
else:
  print("Invalid input")

num=int(input("Enter the number"))
if(num>0):
  print("POSITIVE")
elif(num<0):
  print("NEGATIVE")
else:
  print("ZERO")

username=input("Enter the username")
password=input("Enter the password")
if(username=="admin"):
  if(password=="1234"):
    print("Login Successfull")
  else:
    print("Login Failed")
else:
  print("Login Failed")

a=input("Enter the first side")
b=input("Enter the second side")
c=input("Enter the third side")
if(a+b>c):
  print("valid triangle")
elif(b+c>a):
  print("Valid Triangle")
elif(a+c>b):
  print("valid Triangle")
else:
  print("Invalid Triangle")

weight=float(input("Enter the weight in killogram "))
height=float(input("Enter the height in meter "))
BMI=float(weight/(height**2))
if(BMI>30):
  print("Obesity")
elif(BMI>=25 and BMI<=29.9):
  print("Over weight")
elif(BMI>=18.5 and BMI<=24.9):
  print("Normal Weight")
elif(  BMI<18.5):
  print("Under Weight")
else:
  print("Invalid Input")

print("Enter your card")
pin=int(input("Enter the pin"))
choice=char
if(pin=="1234"):
  choice=int(input("Choose the Options"))
  print("Check Balance")
  print("Deposit Money")
  print("Withdraw Money")
  if(choice=="Check Balance"):
    print("Your Balance is 123456")
  elif(choice=="Deposit Money"):
    print("Please Place the cash on machine")
  elif(choice=="Withdraw Money"):
    print("Enter the amount for withdraw")
else:
  print("TRY AGAIN LATER")

age=int(input("Enter the age"))
if(age>=60):
  print("Senior")
elif(age>=20 and age<=59):
  print("ADULT")
elif(age>=13 and age<=19):
  print("TEENAGER")
elif(age>=5 and age<=12):
  print("Child")
elif(age>=2 and age<=4):
  print("TODDLER")
elif(age>=0 and age<=1):
  print("INFANT")
else:
  print("Invalid Age")

day=int(input("Enter the day of week"))
if(day==1):
  print("MONDAY")
elif(day==2):
  print("TUESDAY")
elif(day==3):
  print("WEDNESDAY")
elif(day==4):
  print("THURSDAY")
elif(day==5):
  print("FRIDAY")
elif(day==6):
  print("SATURDAY")
elif(day==7):
  print("SUNDAY")
else:
  print("Invalid day")