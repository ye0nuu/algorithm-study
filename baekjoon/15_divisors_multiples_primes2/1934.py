# BOJ 1934번: 최소공배수 
# URL: https://www.acmicpc.net/problem/1934
# 분류: 수학, 정수론, 유클리드 호제법 
# 난이도: 브론즈 1
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 두 자연수 A, B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - math 모듈을 사용하여 A, B의 최대공약수를 구한 뒤, 두 수의 곱을 최대공약수로 나누어 최소공배수를 구한다. 

import math

T = int(input())

for _ in range(T):
  A, B = map(int, input().split())

  LCM = A * B // math.gcd(A, B)
  print(LCM)