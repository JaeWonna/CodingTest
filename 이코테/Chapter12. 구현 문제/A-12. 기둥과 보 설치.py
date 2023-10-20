def check_possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: #기둥
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1: #보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,cmd = frame
        if cmd == 1: #설치
            answer.append([x,y,stuff])
            if not check_possible(answer):
                answer.remove([x,y,stuff])
        elif cmd == 0: #삭제
            answer.remove([x,y,stuff])
            if not check_possible(answer):
                answer.append([x,y,stuff])
    return sorted(answer)
            
