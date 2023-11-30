data = input()
result = []
value = 0

for i in data:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

# 0이면 아무것도 쓰지 않는다
if value != 0:
    result.append(str(value))
print(''.join(result))
