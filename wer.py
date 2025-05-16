n = int(input("Enter number:"))
rev = 0
temp_n = n  # Store a copy of n to reverse

while temp_n > 0:
    dig = temp_n % 10
    rev = rev * 10 + dig
    temp_n //= 10

print(rev)

final_list = []
while rev > 0:
    l = rev % 10
    s = (rev // 10) % 10 if rev // 10 > 0 else 0  # Handle cases where there's no second digit

    if s != 0 or rev // 10 > 0: # Avoid leading zeros unless it is the last digit
        final_list.append([s, l])

    rev //= 10

final_list.reverse()
print(final_list)