def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2+1):  # 1부터 길이//2까지 순차적으로 검사한다
        compressed = ''
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]: # 같으면 count값만 1 증가
                count += 1
            else: # 서로 다를 경우에 출력 후 prev 바꾼다
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1 #다시 초기화
        
        # 마지막 값이 그 전 값과 같고 아직 출력이 안되고 for문이 끝났을 경우
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

s = [
    "aabbaccc",	
    "ababcdcdababcdcd",	    
    "abcabcdede",	
    "abcabcabcabcdededededede",	
    "xababcdcdababcdcd"	
]

for x in s:
    print(solution(x))
