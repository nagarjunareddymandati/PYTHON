t=(1,'nag',2,'sai',3,'geeta',4,'janu');
print(t);
print("Access the items in tuple");
print(t[2]);
print(t[-1]);
print(t[:-1]);
print(t[::-1]);
if 'nag' in t:
    print(" 'nag' is in the tuple");
else:
    print(" 'nag' is not in the tuple");

print("convert list to tuple");
l=[1,2,3];
t=tuple(l);
print(t);

l1=list(t);
print(l1);
l1[1]='dad';
t=tuple(l1);
print(t);
