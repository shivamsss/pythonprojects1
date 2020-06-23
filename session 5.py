from builtins import range

# print('while loop')
# i=1
# while i<=10:
#     print("i is",i)
#     i=i+1
# print("++++++++++++++++++++++++++++++++++++++++++++++")
#
# for i in range(0,4):
#     print('i is ',i)
#     i+=1
# print("++++++++++++++++++++++++++++++++++++++++++++++")
#
# for i in range(0,4):
#     print('i is ',i)
#     for j in range(0,5):
#         print('j is ',j)
# print("++++++++++++++++++++++++++++++++++++++++++++++")

# reverse of the loop
#
# for i in reversed(range(10+1)):
#     print('i is ',i)



my_floor = input("Enter your Floor: ")

for i  in range(1,11,1):
    if(i == my_floor):
        print('floor arrived : ',i)



