# BOJ 1735번: 분수 합 
# URL: https://www.acmicpc.net/problem/1735
# 분류: 수학, 정수론, 유클리드 호제법 
# 난이도: 실버 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램 작성
# 기약분수 - 더 이상 약분되지 않는 분수 

# ✅ 내 풀이 아이디어:
# - 두 분수를 입력받고 두 분모의 최소공배수를 구해 분모를 통분한다.
# - 각 분수의 분자에도 최소공배수//원래분모 를 곱해 통분한다.
# - 통분된 두 분수를 더해 새로운 분수를 만들고, 새 분수의 최대공약수를 구한다.
# - 분수의 분자와 분모를 최대공약수로 나눠 기약분수로 만든다. 

import math

i, j = map(int, input().split())
x, y = map(int, input().split())

lcm = j * y // math.gcd(j, y)

A = i * (lcm//j) + x * (lcm//y)
B = lcm

gcd = math.gcd(A, B)
A //= gcd
B //= gcd

print(f"{A} {B}")