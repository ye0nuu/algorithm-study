# BOJ 10872번: 팩토리얼 
# URL: https://www.acmicpc.net/problem/10872
# 분류: 수학, 구현 
# 난이도: 브론즈 3
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 0보다 크거나 같은 정수 N이 주어질 때, N!를 출력하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# -

N = int(input())

fac = 1
for i in range(2, N+1):
  fac *= i

print(fac)