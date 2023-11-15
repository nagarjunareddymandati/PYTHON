empty_dict={};
print(empty_dict);
my_dict = {'name': 'Nag', 'age': 25, 'city':'Markapur'}
print(my_dict)
print("Name is :", my_dict['name']);
print("Age is : ", my_dict['age']); 
print("City is : ", my_dict['city']);
my_dict["country"]="USA"
print(my_dict);                     
my_dict["age"]=26
print(my_dict)                   
del my_dict["city"]
print(my_dict)                      
if "name" in my_dict:
    print('Key Exists');
else:
    print('Key Does not exist');


