num1=int(input("enter the value of number 1 : "))
num2=int(input("enter the value of number 2 : "))
operation=input("enter the operation : ")
if(operation =='+'):
    print(num1+num2)
elif(operation =='-') :
    print(num1-num2)
elif(operation =='*') :
    print(num1*num2)
elif(operation =='/') :
    print(num1/num2)
elif(operation =='%') :
    print(num1%num2)
elif(operation =='^') :
    print(num1**num2)
else:
    print("enter a valid operaion")