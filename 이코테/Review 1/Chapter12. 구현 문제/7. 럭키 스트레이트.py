data = list(map(int, input()))
n = len(data)

result1 = sum(data[:n//2])
result2 = sum(data[n//2:])

if result1 == result2:
    print('LUCKY')
else:
    print('READY')
