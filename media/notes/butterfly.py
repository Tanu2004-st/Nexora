n = int (input("Enter a number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("\u2764\uFE0F", end = " ")
   
    for j in range(1,2*(n-i)+1) :
        print(" ",end =" ")
    for j in range(1, i + 1):
       print("\u2764\uFE0F", end=" ")
    print()
for i in range(n,0,-1):
    for j in range (1,i+1):
        print("\u2764\uFE0F",end =" ")
    for j in range(1,2*(n -i)+1):
        print(" ",end = " ")
    for j in range(1,i+1) :
         print("\u2764\uFE0F",end =" ")
    print()            