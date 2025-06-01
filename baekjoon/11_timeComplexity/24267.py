# BOJ 24267번: 알고리즘 수업 - 알고리즘의 수행 시간 6
# URL: https://www.acmicpc.net/problem/24267
# 분류: 수학, 구현, 시뮬레이션
# 난이도: 브론즈 2
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행시간을 예제 출력과 같은 방식으로 출력 
# MenOfPassion(A[], n) {
#    sum <- 0;
#    for i <- 1 to n - 2
#       for j <- i + 1 to n - 1
#         for k <- j + 1 to n
#           sum <- sum + A[i] x A[j] x A[k]; # 코드1
#    return sum;
# }

# ✅ 내 풀이 아이디어:
# - 경우의 수를 구하는 알고리즘이라고 접근하면 수행횟수는 (n * (n-1) * (n-2)) / 3! 이 된다.
# - 반복문이 3개 있으므로 3차식으로 표현 가능하다. 

n = int(input())

count = (n * (n-1) * (n-2)) // 6

print(count)
print(3)