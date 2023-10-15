n,m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
array = [0]*11

for i in data:
    array[i] += 1

for i in range(1,m+1):
    n -= array[i] # n => b가 선택(갱신)
    result += array[i] * n

print(result)
