def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for i in array:
            if i > mid:
                total += i-mid
        
        if total >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

n,m = map(int, input().split())
data = list(map(int, input().split()))
start = 0
end = max(data)
print(binary_search(data, m, start, end))
