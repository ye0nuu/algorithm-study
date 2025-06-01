# BOJ 24266번: 알고리즘 수업 - 알고리즘의 수행 시간 5
# URL: https://www.acmicpc.net/problem/24266
# 분류: 수학, 구현, 시뮬레이션
# 난이도: 브론즈 3
# 풀이 시간: 2분

# ✅ 문제 설명 요약:
# 입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행시간을 예제 출력과 같은 방식으로 출력 
# MenOfPassion(A[], n) {
#    sum <- 0;
#    for i <- 1 to n
#       for j <- 1 to n
#         for k <- 1 to n
#           sum <- sum + A[i] x A[j] x A[k]; # 코드1
#    return sum;
# }

# ✅ 내 풀이 아이디어:
# - 수행횟수는 n만큼 반복문을 3번 도므로 n의 3제곱번이 된다.
# - 시간복잡도가 O(n^3)이므로 3차식으로 표현 가능 

n = int(input())

print(n**3)
print(3)