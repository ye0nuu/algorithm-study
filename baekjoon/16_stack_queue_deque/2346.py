# BOJ 2346번: 풍선 터뜨리기 
# URL: https://www.acmicpc.net/problem/2346
# 분류: 자료 구조, 덱 
# 난이도: 실버 3
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 1번부터 N번까지 N개의 풍선이 원형으로 놓여 있다.
# i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다.
# 각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 규칙에 맞춰 터뜨린다.
# 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내 그 종이에 적혀있는 값만큼 이동해 다음 풍선을 터뜨린다.
# 양수가 적혀있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동, 이미 터진 풍선은 빼고 이동한다.

# ✅ 내 풀이 아이디어:
# - collections의 deque 모듈 활용, N을 입력받고 풍선숫자를 deque로 입력받는다. 순서를 저장하기 위해 enumerate로 인덱스번호+1도 함께 저장한다.
# - 순서를 저장하기 위한 seq 배열을 생성하고 ball이 비기 전까지 풍선제거 과정을 반복한다.
# - 맨 앞의 풍선을 빼서 저장된 순서를 seq에 추가하고, 풍선 숫자는 n에 저장한다.
# - 제거 후 ball이 비었으면 반복을 멈추고, n이 0보다 크다면 오른쪽으로 n만큼 회전한다.
# - 아니라면 왼쪽으로 n만큼 회전한다.
# - 최종 저장된 seq 배열을 형식에 맞추어 출력한다.

from collections import deque

N = int(input())
ball = deque((i+1, val) for i, val in enumerate(map(int, input().split())))
seq = []

while ball:
  pop_ball = ball.popleft()
  seq.append(pop_ball[0])
  n = pop_ball[1]

  if not ball:
    break
  if n > 0:
    ball.rotate(-(n-1))
  else:
    ball.rotate(-n)

print(' '.join(map(str, seq)))