# str1 = "hello "
# str2 = "world"
# FinalString = str1+str2 #string concatination
# StringLength = len(FinalString) #to find the length of the string
# print(FinalString)
# print(StringLength)
# print(str1+str2)
# print(str1+" "+str2)
#indexing in strings
# str3 ="aizen Souske"
# print(str3[0])#we get the character at the particular index in the string...
#Strings are immutable
#slicing in strings : accessing part of string str[starting_index : ending_index]   
# print(str3[1:4])#prints the characters of the string form the index 1 till index 3
# print(str3[:5])#this is same as printing from index 0 till index 5
# print(str3[0:])#this is same as printing from index 0 to index len[str]
#slicing using negative index : it is like index of first character of the string is (-str(len)) if len of str is 5 the index of first character is -5 and the index of last character is 0
# print(str3[-len(str3): -1])#here we wont get the last character ..
# print(str3[-len(str3): ])#here we get the full string using negative indexing
#string functions
# print(str3.endswith("e"))#checks wether the string ends with the given character or not.
# print(str3.endswith("ouske"))#checks wether the string ends with the given sequence or not.
# print(str3.capitalize())#captialize the first character of the string
# print(str3)
# print(str3.replace("aizen","Aizen"))#prints the value of the string replacing the value provided of the string with new value.. 
# print(str3.replace("e","k"))#it is possible the change multiple characters 
# print(str3.replace("e","kei"))#it is possible the change multiple characters 
# print(str3)#prints the value of string
# print(str3.find("zen"))#gives the index value of the first letter of the given sequence of the first occurence
# print(str3.find("z"))#gives the index value of the character of first occurence
# print(str3.count("Souske"))#gives the no of times did the given word occur in the string
# print(str3.count("e"))#gives the no of times did the given character occur in the string
#if we want  to modify the string we can perform the action 
# str3 = str3.replace("aizen","Aizen")#it is possible to change the value of string like this.. here the string value is replaced but not changed..
# print(str3)
#question 1
Fname = input("enter your first name")
print(len(Fname))
#question 2
String1 = "$ is the symbol dollar . $ is the currency of united states of america . $ is also known for its dominance in the international exchange of currency.its all $$$$$"
print(String1.count("$"))