n = input("Enter the number: ")

length = len(str(n))

if length < 8:
    print("Please enter more than 8 digits.")
else:
    print(n[3])
    