# BOJ 18258번: 큐 2
# URL: https://www.acmicpc.net/problem/18258
# 분류: 자료 구조, 큐
# 난이도: 실버 4
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성
# 명령은 총 여섯가지
# - push X: 정수 X를 큐에 넣는 연산
# - pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력 
# - size: 큐에 들어있는 정수의 개수를 출력 
# - empty: 큐가 비어있으면 1, 아니면 0을 출력 
# - front: 큐의 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1 출력
# - back: 큐의 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1 출력 

# ✅ 내 풀이 아이디어:
# - collections의 deque를 이용해 popleft() 사용해 속도 높임 

import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
for _ in range(N):
  inputs = sys.stdin.readline().split()
  comm = inputs[0]

  if comm == 'push':
    queue.append(inputs[1])

  elif comm == 'pop':
    if queue:
      sys.stdout.write(str(queue.popleft()) + '\n')
    else:
      sys.stdout.write('-1\n')
  elif comm == 'size':
    sys.stdout.write(str(len(queue)) + '\n')

  elif comm == 'empty':
    if not queue:
      sys.stdout.write('1\n')
    else:
      sys.stdout.write('0\n')

  elif comm == 'front':
    if queue:
      sys.stdout.write(str(queue[0]) + '\n')
    else:
      sys.stdout.write('-1\n')

  elif comm == 'back':
    if queue:
      sys.stdout.write(str(queue[-1]) + '\n')
    else:
      sys.stdout.write('-1\n')