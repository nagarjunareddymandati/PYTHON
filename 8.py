def find_largest(n1,n2,n3):
    if(n1 > n2) and (n1 > n3):
        largest=n1
    elif(n2 > n1) and (n2 > n3):
        largest = n2
    else:
        largest = n3
    return largest
n1 = int(input("Enter first number: "));
n2 = int(input("Enter second number: "));
n3 = int(input("Enter third number: "));
print ("Largest number is",find_largest(n1,n2,n3))