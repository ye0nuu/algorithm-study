# BOJ 2485번: 가로수 
# URL: https://www.acmicpc.net/problem/2485
# 분류: 수학, 정수론, 유클리드 호제법 
# 난이도: 실버 4
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램 작성
# 단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.

# ✅ 내 풀이 아이디어:
# - 이미 심어진 나무들의 위치를 저장할 tree 배열을 만들어 입력받는다.
# - 나무 위치를 정렬하고 나무 사이의 거리를 gap 배열에 저장한다.
# - 거리들의 공통 최소공약수를 구해 같은 간격이 되기 위한 거리를 구한다.
# - 해당 거리를 유지하며 심어질 나무 수를 구하고 현재 심어져 있는 나무 수를 빼 심어야할 나무 수를 구해 출력한다.ㄴ

import math

N = int(input())

tree = []
for _ in range(N):
  tree.append(int(input()))

tree.sort()
gap = [tree[i+1]-tree[i] for i in range(N-1)]

gcd = gap[0]
for i in range(1, len(gap)):
  gcd = math.gcd(gcd, gap[i])

count = (tree[N-1] - tree[0]) // gcd + 1 - N

print(count)