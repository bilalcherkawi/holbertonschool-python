#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str=""
a=number%10
if a > 5:
   str="and is greater than 5"
elif a==0:
   str="and is 0"
elif 0 < a < 6
   str="and is less than 6 and not 0"
print("Last digit of" + number+ "is"+ a+ str) 
