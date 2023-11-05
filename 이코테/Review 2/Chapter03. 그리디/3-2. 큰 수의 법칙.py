n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
total,count = 0,0
first,second = data[n-1],data[n-2]

count += (m // (k+1)) * k
count += m % (k+1)

total += first * count
total += second * (m-count)

print(total)
