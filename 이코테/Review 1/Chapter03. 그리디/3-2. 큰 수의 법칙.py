n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = 0
count = (m//(k+1))*k # 몫
count += m % (k+1) # 나머지

result = 0
result += (count) * first
result += (m-count) * second
print(result)
