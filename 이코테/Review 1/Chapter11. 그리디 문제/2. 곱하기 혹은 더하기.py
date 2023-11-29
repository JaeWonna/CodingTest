data = list(map(int, input()))
result = data[0]

for i in data[1:]:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
