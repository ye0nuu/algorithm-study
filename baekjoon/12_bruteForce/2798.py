# BOJ 2798번: 블랙잭 
# URL: https://www.acmicpc.net/problem/2798
# 분류: 브루트포스 알고리즘 
# 난이도: 브론즈 2
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력 

# ✅ 내 풀이 아이디어:
# - N, M을 입력받고 카드의 숫자는 리스트로 입력받는다.
# - 중복된 카드를 뽑지 않도록 3중 중첩반복문을 순회하며 카드의 합을 구하고, M을 넘지 않으면서 가장 큰 합보다 큰 경우 새로 값을 저장한다.
# - 최종 저장된 조건을 만족하는 최대합을 출력한다. 

N, M = map(int, input().split())

cards = list(map(int, input().split()))

sum = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      cal = cards[i] + cards[j] + cards[k]
      if cal <= M and cal > sum:
        sum = cal

print(sum)