# BOJ 2444번: 별 찍기 -7
# URL: https://www.acmicpc.net/problem/2444
# 분류: 구현
# 난이도: 브론즈 3
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 예제를 보고 규칙을 유추한 뒤 별 찍기

# ✅ 내 풀이 아이디어:
# - 반복문으로 N 이용해 공백과 별 찍음

N = int(input())

for i in range(1, N+1):
  print(" "*(N-i) + "*"*(2*i-1))

for i in range(N-1, 0, -1):
  print(" "*(N-i) + "*"*(2*i-1))