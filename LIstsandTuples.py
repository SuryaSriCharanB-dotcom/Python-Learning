#lists in python
marks=[23.4,24,78.9,267]
print(marks)#prints the contents in the list 
print(type(marks))#prints the data type of the variable marks
print(len(marks))#gives you the length of the list
print(marks[0])#prints the element at the index 0
print(marks[len(marks)-1])#prints the element at the last index
print(marks[1])#prints the element at the index 1
# strings are Immutable
# litst are mutable
#unlike arrays in java which accepts only a single data type , here in python lists can accepts multiple datatypes in a single list
student=["Ichigo",101,98.7,True]#storing multiple types of data ina single list
print(student)#printing the values stored in the list = student..
student[0] ="Orihime" #we can change the value of data in a particular index is possible in list
print(student)
student [0] = 127 #we can also replace the data with diffrent data type as well 
print(student)
#list slicing
#it is the same as string slicing
#list methods
student.append(27)
print(student)
student.append("yahwach")
print(student)
marks.sort()#we can sort the list in ascending order, also sort() funcion will not return anything
print(student)#it gives none as output
print(marks)
# student.sort()#we cannot sort a list with diffrent datatypes 
# print(student)#we get a type error 
marks.sort(reverse=True)#this well arrainge the list in descending order
print(marks)#the output will be in descending order
marks.reverse()#this will reverse the list
print(marks)#the output will be reverse of the list
#sorting also applicabe on strings
names=["Ichigo","Orihime","Uryu","Chad","Rukia","Aizen","Yamamoto","Yoruichi", "Byakuya","Renji","Kenpachi","Toshiro","Gin","Kisuke","Grimmjow","Ulquiorra","Nelliel"]
print(names)
# names.sort()#this will sort the list in ascending order
names.sort()
print(names)
names.sort(reverse=True)#this will sort the list in descending order
print(names)
names.reverse() #this will reverse the list
print(names)#prints the reverse of the list
#inserting elements in a list
#we create a new list and insert the elements in the list
OnePiece=["Luffy","Zoro","Nami","Usopp","Sanji","Chopper","Robin","Franky","Brook","Jinbe"]
print(OnePiece)
OnePiece.insert(3,"Vivi")#this will insert the element at the index 3
print(OnePiece)
#removing elements from the list
#pop() method is used to remove the element from the list
OnePiece.pop()#this will remove the last element from the list
print(OnePiece)
OnePiece.pop(3)#this will remove the element at the index 3
print(OnePiece)
#remove() method is used to remove a particular element from the list
OnePiece.remove("Robin")#this will remove the element "Usopp" from the list
print(OnePiece)
#del keyword is used to delete the element from the list
del OnePiece[5]#this will remove the element at the index 5
print(OnePiece)
#clear() method is used to clear the list
OnePiece.clear()#this will clear the list
print(OnePiece)
#copy() method is used to copy the list
OnePiece=["Luffy","Zoro","Nami","Usopp","Sanji","Chopper","Robin","Franky","Brook","Jinbe"]
print(OnePiece)
strawhat=OnePiece.copy()#this will copy the list OnePiece to strawhat
print(strawhat)
#list concatenation
#we can concatenate two or more lists using + operator
#we can also use extend() method to concatenate two or more lists
#we can also use append() method to concatenate two or more lists
#we can also use the * operator to repeat the list
