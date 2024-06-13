def solution(n, s):
    if n > s:
        return [-1]
    
    quotient = s // n  # 몫
    remainder = s % n  # 나머지
    
    answer = [quotient] * (n - remainder) + [quotient + 1] * remainder
    
    return answer

# 예시 테스트
print(solution(2, 8))  # [4, 4]
