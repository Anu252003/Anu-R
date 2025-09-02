a = int(input("Enter a number: "))

if a % 2 == 0:  
    a -= 1

num = 1
for i in range(a):
    print(num, end=" ")
    num += 2
