data = input()
result = []
total = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        total += int(x)

result.sort()

if total != 0:
    result.append(str(total))

print(''.join(result))

