data = list(map(int, input()))
result = data[0]

for i in data[1:]:
    plus = result + i
    mul = result * i
    result = max(plus, mul)

print(result)
