def solution(n, m, section):
    answer = 1
    start = section[0]
    for i in section:
        if start <= i <= start+m-1:
            continue
        else:
            start = i
            answer+=1
    return answer