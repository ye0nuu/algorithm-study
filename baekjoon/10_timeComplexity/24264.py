# BOJ 24264번: 알고리즘 수업 - 알고리즘의 수행 시간 3
# URL: https://www.acmicpc.net/problem/24264
# 분류: 수학, 구현, 시뮬레이션, 사칙연산 
# 난이도: 브론즈 3
# 풀이 시간: 2분

# ✅ 문제 설명 요약:
# 입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행시간을 예제 출력과 같은 방식으로 출력 
# MenOfPassion(A[], n) {
#    sum <- 0;
#    for i <- 1 to n
#        for j <- 1 to n
#          sum <- sum + A[i]; # 코드1
#    return sum;
# }

# ✅ 내 풀이 아이디어:
# - n까지 반복되는 반복문이 2개 있으므로 수행횟수는 n*n 회가 된다.
# - 시간복잡도가 O(n^2)으로 2차식으로 표현 가능하므로 차수는 2가 된다.

n = int(input())

print(n*n)
print(2)