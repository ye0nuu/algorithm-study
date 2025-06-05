# BOJ 11050번: 이항 계수 1
# URL: https://www.acmicpc.net/problem/11050
# 분류: 수학, 구현, 조합론 
# 난이도: 브론즈 1
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 자연수 N과 정수 K가 주어졌을 때, 이항 계수 (N K)를 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - math 모듈의 factorial 함수를 이용해 이항계수를 계산해 출력한다. N! // K! * (N-K)!

import math

N, K = map(int, input().split())

fac = math.factorial(N) // (math.factorial(K) * math.factorial(N-K))
print(fac)