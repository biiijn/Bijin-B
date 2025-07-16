num = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

div_count = {}
for i in range(1, 10):
    div_count[i] = 0

for number in num:
    for divisor in range(1, 10):
        if number % divisor == 0:
            div_count[divisor] += 1

print(div_count)               