#Question-1
# j=0
# while(j==0):
#     print("choose a color form the following \nred\nyellow\ngreen")
#     light = input("enter the signal light : ")
#     print()
#     if(light=="red" or light == "yellow" or light == "green"):
#         k=0
#         while(k == 0):
#             if(light == "red"):
#                 print("current colour is red..the next colour is yellow...\n")
#                 light = "yellow"
#             elif(light == "yellow"):
#                 print("current colour is yelow .. the next colour is green...\n")
#                 light = "green"
#             elif(light == "green"):
#                 print("current colour is green... loop ends...\n")
#                 k=1
#                 j=1
#     else:
#         print("enter a valid colour..\n \n ")

#programming in python is diffrent form other language is Its indentation ,Yes! python Uses indentation to separate the blocks of code.
#Question-2

# k =0
# while(k==0):
#     marks =  int(input("enter marks : "))
#     if(0<=marks<=100):
#         if(marks>=90):
#             print("Grade = A")
#             k=1
#         elif(marks>=80):
#             print("Grade = B")
#             k=1
#         elif(marks>=70):
#             print("Grade = C")
#             k=1
#         else:
#             print("Grade= D")
#             k=1
#     else:
#         print("enter valid marks...")
#Question-3
# num = int(input("enter a number : "))
# if(num%2==0):
#     print("it is even")
# else:
#     print("it is odd")
#Question-4
# num1= int(input("enter num 1 :"))
# num2= int(input("enter num 2 :"))
# num3= int(input("enter num 3 :"))
# if(num1>num2):
#     if(num1>num3):
#         print(f'{num1} is greatest ')
# elif(num2>num3):
#     print(f'{num2} is greatest ')
# else:
#     print(f'{num3} is the greatest ')
# question-5
# num = int(input("enter a number : "))
# if(num%7==0):
#     print("it is divisible by 7")
# else:
#     print("it is not divisible by 7")
#hw

num1= int(input("enter num 1 :"))
num2= int(input("enter num 2 :"))
num3= int(input("enter num 3 :"))
num4= int(input("enter num 4 :"))
if(num1>=num2 and num1>=num3 and num1>=num4):
    greatest = num1
elif(num2>num1 and num2 >=num3 and num2>num4):
    greatest=num2
elif(num3 >= num1 and num3 >= num2 and num3 >=num4):
    greatest = num3
else:
    greatest = num4
count=0
if(greatest == num1):
    count+=1
if(greatest == num2):
    count+=1
if(greatest == num3):
    count+=1
if(greatest == num4 ):
    count+=1
if(count>1):
    print(f'theere are multiple greatest numbers:{greatest}')
else:
    print(f'greatest number is {greatest}')