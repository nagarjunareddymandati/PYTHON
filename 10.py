def stars_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for k in range(i+1):
            print("*", end=" ")
        print()
if __name__ == "__main__":
 n = int(input("Enter the size of the stars pattern: "))
stars_pattern(n)