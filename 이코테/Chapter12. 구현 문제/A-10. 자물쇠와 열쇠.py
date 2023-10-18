# 2차원 리스트 회전
def rotate(a):
    x = len(a)
    y = len(a[0])
    result = [[0]*x for _ in range(y)]

    for i in range(x):
        for j in range(y):
            result[j][x-i-1] = a[i][j]
    return result

# 리스트의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2): # (3,3)부터 (5,5)의 면적인 가로3, 세로3 가운데키 검사
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    # 3배로 커진 lock리스트의 정 한 가운데에 조준해서 lock만들기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate(key)

        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
print(solution(key, lock))
