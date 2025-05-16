n = int(input("Enter the number: "))

num = 1
count = 6

for i in range(1,n+1):
    for j in range(1,i+1):
        if i == j:
            print(num,end="")
            num += 1
            continue
        if i != j:
            print(" ",end="")
            continue

        # for k in range(6,count):
        #     count += 1
        #     print(count)

        if i == 2 and j == 1:
            print("*",end="")
            
        
    print(" ")