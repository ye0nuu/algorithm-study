# BOJ 2751번: 수 정렬하기 2
# URL: https://www.acmicpc.net/problem/2751
# 분류: 정렬
# 난이도: 실버 5
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬 

# ✅ 내 풀이 아이디어:
# - N을 입력받고, N개의 숫자를 입력받아 배열에 저장
# - input()의 속도가 느리므로 sys를 import해 sys.stdin.readline() 사용 
# - .sort() 함수로 숫자 배열 오름차순 정렬, 형식에 맞춰 출력 

import sys

N = int(input())

num = []
for _ in range(N):
  num.append(int(sys.stdin.readline()))

num.sort()

for n in num:
  print(n)