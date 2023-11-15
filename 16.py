f1=input("Enter the name of the first text file: ")
f2=input("Enter the name of the second text file: ")
with open(f1, 'r') as file1:
  content = file1.read()
  with open(f2, 'w') as file2:
        file2.write(content)
print("the file concates with file1 to file2",f1,f2);