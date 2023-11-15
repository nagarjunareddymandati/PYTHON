l=[1,2,3,4,5]
print("List is ",l);
print(len(l));
print(type(l));
print("Append the items");
l.append(6);
l.append("nag");
l.append("sai");
l.append(4606);
print("after Append",l);
print("Insert item at 1st position");
l.insert(0,"hello");
print("After insertion",l)
print("Delete an element from list")
del l[3];
print("After deletion of element",l)
print("Slicing a list")
print(l[:]);
print(l[::-1]);
print("Multiply all elements in list by 2");
for i in range(len(l)):
    l[i]=l[i]*2;
print(l);


