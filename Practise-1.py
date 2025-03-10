num = int(input("enter the value : "))
#right angled triangle:
# for i in range(1,num+1):
#     print("* "*i)
#inverted right angle triangle
# for i in range(num,0,-1):
#     print("* "*i)
#using numbers
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#inverse triangle numbers
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#piryamid
# for i in range (1,num+1):
#     print(" "*(num-i),end="")
#     print("* "*i)
# Diamond
# for i in range (1,num+1):
#     print(" "*(num-i),end="")
#     print("* "*i)
# for j in range (num-1,0,-1):
#     print(" "*(num-j),end ="")
#     print("* "*j)
#hollow square
# for i in range(1,num+1):
#     if(i==1 or i==num):
#         print("* "*num)
#     else:
#         print("*"+"  "*(num-2)+" *")
#hollow pyramid
# for i in range (1,num+1):
    # if (i == 1 or i == num):
        # print(" "*(num-i),end="")
        # print("* "*i)
    # else:
        # print(" "*(num-i),end="")
        # print("*"+" "*(2*i-3)+"*")
#inverted pyramid
# for j in range (num-1,0,-1):
#     print(" "*(num-j),end ="")
#     print("* "*j)
#hollow diamond
# for i in range(1,num+1):
#     if i==1:
#         print(" "*(num-i)+"*")
#     else:
#         print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
# for i in range(num-1,0,-1):
#     if i==1:
#         print(" "*(num-i)+"*")
#     else:
#         print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
#Hollow diamomd with diagonal
# for i in range(1,num+1):
#     if i == 1 or i== num:
#         print(" "*(num-i)+"* "*i)
#     else:
#         print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
# for i in range (num-1,0,-1):
#     if i==1:
#         print(" "*(num-i)+"*")
#     else:
#         print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
#Hour glass
# naa telivi inthey kada nee jathini dengutha gaa naa bhashalu aaru sare avi dengulu avunu mari 
# oopiri titthulu undavule gudda balupu untadhi le jitthula manishi alpulu le nenu erripukuni ley 
# for i in range(num,0,-1):
#     print(" "*(num-i)+"* "*i)
# for i in range(2,num+1):
#     print(" "*(num-i)+"* "*i)
#hour glass -2
# if(num%2==0):
#     last=num-1
# else:
#     last=num
# for i in range(last,0,-2):
#     print(" "*(num-i)+"* "*i)
# for i in range(3,last+1,2):
#     print(" "*(num-i)+"* "*i)
#X- pattern
# for i in range (num,0,-1):
#     if(i==1):
#         print(" "*(num-i)+"*")
#     else:    
#         print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
# for i in range(2,num+1):
#     print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
#butterfly pattern
for i  in range(1,num+1):
    print("* "*i+"  "*(num-i)+"* "*i)
for i in range(num,0,-1):
    print("* "*i+"  "*(num-i)+"* "*i)
#butterfly pattern-2
for i  in range(1,num+1):
    print("* "*i+"  "*(num-i)+"* "*i)
for i in range(num-1,0,-1):
    print("* "*i+"  "*(num-i)+"* "*i)