# BOJ 13241번: 최소공배수 
# URL: https://www.acmicpc.net/problem/13241
# 분류: 수학, 정수론, 유클리드 호제법 
# 난이도: 실버 5
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 두 수에 대하여 최소공배수를 구하는 프로그램을 작성 

# ✅ 내 풀이 아이디어:
# - math 모듈을 사용하여 A, B의 최대공약수를 구한 뒤, 두 수의 곱을 최대공약수로 나누어 최소공배수를 구한다. 

import math

A, B = map(int, input().split())

lcm = A * B // math.gcd(A, B)
print(lcm)