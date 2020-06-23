# tuple, list and string -> indexing
# set and dictionary     -> hashing
#
# 1.
# Concatenation
# 2.
# Repetition
# 3.
# Membership
# testing
# 4.
# Indexing
# 5.
# Slicing


# tuple1 = (11,12,13,14)
# #1 concatenation
# print("concatination of tuple",tuple1+(10,9,8,7))
#
# #2 repetition
# repeatedtuple = tuple1*2
# print("repitation is ",repeatedtuple)
#
# #3MembershipTesting
# print(11 in tuple1)
# print(10 not in tuple1)
#
# print()
#
# #4 Slicing
# print(tuple1[0:2])
#
# #5 Indexing
# print(tuple1[0])
# print(tuple1[1])
#
#
# print("-----------------------------------------------------------------------------------------------------------------")
# list1 = [11,12,13,14]
# #1 concatenation
# print("concatination of list",list1+[10,9,8,7])
#
# #2 repetition
# list2 = list1*2
# print("repitation is ",list2)
#
# #3MembershipTesting
# print(11 in list1)
# print(10 not in list2)
#
# print()
#
# #4 Slicing
# print(list1[0:2])
#
# #5 Indexing
# print(list1[0])
# print(list1[1])

print("--------------------------------------------------------------------------------------------------------------------------")
#
# set1 = {11,12,13,14}
# print(type(set1))
#1 concatenation
#print("concatination of set",set1+{10,9,8,7})

#2 repetition
# set2 = set1*2
# print("repitation is ",set2)

#3MembershipTesting
# print(11 in set1)
# print(10 not in set1)
#
# print()

#4 Slicing
# print(set1[0:2])

#5 Indexing
# print(set1[0])
# print(set1[1])

#
# print("---------------------------------------------------------------------------------------------------------------")
#
# name = "Shivam"
# print(type(name))
# #1 concatenation
# print("concatination of string",name+" sharma")
#
# #2 repetition
# name = name*2
# print("repitation is ",name)
#
# #3MembershipTesting
# print('s' in name)
# print('s' not in name)
# print()
#
# #4 Slicing
# print(name[0:2])
#
# #5 Indexing
# print(name[0])
# print(name[1])



# Dictionary

name_dic ={
  'name':'Shivam',
   'age':'22'
}

#concationation

dic1 = {
    'qualification':'BTech'
}
name_dic.update(dic1)
print("Concationation",name_dic)


print('22' in name_dic)
print()