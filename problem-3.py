a=int(input("Enter a number:"))

if a % 2 != 0:
    count = a
else:
    count = a - 1

odd_number = 1
printed = 0

while printed < count:
   
    if printed < count - 1:
        print(odd_number, end=", ")  
    else:
        print(odd_number, end="")    

    odd_number = odd_number + 2
    printed = printed + 1

