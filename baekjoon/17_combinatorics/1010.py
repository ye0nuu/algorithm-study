# BOJ 1010번: 다리 놓기 
# URL: https://www.acmicpc.net/problem/1010
# 분류: 수학, 다이나믹 프로그래밍, 조합론 
# 난이도: 실버 5
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 강 서쪽에는 N개의 사이트(다리짓기 적합한 곳), 동쪽에는 M개의 사이트가 있다.
# 한 사이트에 최대 한 개의 다리만 연결될 수 있고, 서쪽과 동쪽의 사이트를 연결하려고 한다.
# 다리를 최대한 많이 짓고자 하여 서쪽의 사이트 개수 N개만큼 다리를 지으려 한다.
# 다리끼리는 서로 겹쳐질 수 없다고 할 때, 다리를 지을 수 있는 경우의 수를 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - M개 중 N개를 뽑는 경우의 수를 구하는 것과 같으므로 MCN을 구해 출력한다.
# - math 모듈의 factorial 함수를 사용해 구해 출력한다. 

import math

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())

  comb = math.factorial(M) // (math.factorial(N) * (math.factorial(M-N)))
  print(comb)