instagram = "auribises"
print("instagram id is: ",instagram,len(instagram),id(instagram))

list_Of_Id = "shivam","rahul","rohan","arjun"
print("list of Id is:",list_Of_Id,len(list_Of_Id),id(list_Of_Id),type(list_Of_Id))

list_of_images = ("desert","holiday","beach")
print("list of images",list_of_images,len(list_of_images),id(list_of_images),type(list_of_images))

cars = {"skoda","maruti","honda","ferrari"}
print("cars are:",cars,len(cars),id(cars),type(cars))
# in a set we cannot update a single no. because we don't know the index no.and they are unsorted and undexed
# in set simple assignment cannot be done
#cars[0] = "lamborghini"
#print("cars are now ",cars)

bikes = ['honda','hero','yamaha','ducati']
print('bikes are :',bikes,len(bikes),id(bikes),type(bikes))

bikes.append('vespa')
bikes.append('kawasaki')
print("bikes are :",bikes)
bikes.append('honda')
print("bikes are now :",bikes)
bikes.remove('honda')
print("bikes are :",bikes)
bikes.reverse()
print("bikes are :",bikes)
bikes.clear()
print("bikes are :",bikes)

div_of_bikes ={
  "name":"R15",
  "company":"yamaha",
  "year":2018
}

print("dic of bikes is ",div_of_bikes)
list_of_features = ['125cc','slipper cluch','disc brakes']

div_of_bikes['features']=list_of_features
print("dic of bikes is ",div_of_bikes)


name = input("enter name")
print("name is",name)

age = int(input("what is your age"))
print("age is ",age,type(age))