# BOJ 2164번: 카드 2
# URL: https://www.acmicpc.net/problem/2164
# 분류: 자료구조, 큐 
# 난이도: 실버 4
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# N장의 카드가 있다. 각각 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번카드가 제일 위에, N번까드가 제일 아래인 상태로 순서대로 카드가 놓여있다.
# 제일 위에 있는 카드를 바닥에 버리고, 제일 위의 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 이 동작을 카드가 한 장 남을 때까지 반복
# N이 주어졌을 때, 제일 마지막에 남는 카드를 구함 

# ✅ 내 풀이 아이디어:
# - N을 입력받고, cards를 collections의 deque 모듈을 이용해 N까지의 카드를 순서대로 저장
# - cards 배열의 길이가 1이 되기 전까지 반복하며, cards의 맨 앞 요소를 popleft() 하고, 다시 popleft해 맨 뒤에 추가(append)
# - 마지막으로 cards에 남은 하나의 원소 출력 

from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])

while len(cards) > 1:
  cards.popleft()
  cards.append(cards.popleft())

print(cards[0])