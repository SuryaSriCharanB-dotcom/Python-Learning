# print(not False)#true
# print(not True)#false
# a=10
# b= 14
# print(not(a>b))#true
# print (not (a<b))#false
# for i in range (128):
#     print(f"asci value of {i} = {chr(i)}")
val1= input("enter a value : ")
print(type(val1))
name = input("enter your name : ")
age = input("enter your age : ")
marks =input("enter your marks :")
print(f"you name :{name} , ",type(name))
print(f"your age : {age} , ", type(age))
print(f"your marks : {marks} , ", type(marks))

# by default the input function take input as a string
#Here we perform typeconversion inorder to take input in required datatype

name1 = input("enter your name : ")
age1 = int(input("enter your age : "))#*here
marks1 =float(input("enter your marks :"))#*here
print(f"you name :{name1} , ",type(name1))
print(f"your age : {age1} , ", type(age1))
print(f"your marks : {marks1} , ", type(marks1))

#strings
str1 = "Bankai is the final form of the zanpakto"
str2 = "But the two goats aizen and ichigo don't have bankai crushed the quincy king and saved the day ...."
str3 ='''Proud to be a no bankai user 
as the savior of Soul society I Aizen Souske .....'''
#escape sequence characters 
str4 = "to give a tab space in b/w \t the strings "
str5 = "to insert a new line we use \n in the strings"