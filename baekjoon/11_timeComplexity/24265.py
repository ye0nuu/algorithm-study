# BOJ 24265번: 알고리즘 수업 - 알고리즘의 수행 시간 4
# URL: https://www.acmicpc.net/problem/24265
# 분류: 수학, 구현, 시뮬레이션, 사칙연산 
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행시간을 예제 출력과 같은 방식으로 출력 
# MenOfPassion(A[], n) {
#    sum <- 0;
#    for i <- 1 to n - 1
#       for j <- 1 + 1 to n
#        sum <- sum + A[i] x A[j]; # 코드1
#    return sum;
# }

# ✅ 내 풀이 아이디어:
# - 수행횟수: 1부터 n-1까지의 합
# - 시간복잡도가 O(n^2)이므로 차수는 2가 된다.

n = int(input())

count = 0
for i in range(1, n):
  count += i

print(count)
print(2)