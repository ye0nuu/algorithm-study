# BOJ 28279번: 덱 2
# URL: https://www.acmicpc.net/problem/28279
# 분류: 자료 구조, 덱 
# 난이도: 실버 4
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성
# 명령은 총 여덟가지
# - 1 X : 정수 X를 덱의 앞에 넣음
# - 2 X : 정수 X를 덱의 뒤에 넣음
# - 3 : 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력, 없다면 -1 출력
# - 4 : 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력, 없다면 -1 출력
# - 5 : 덱에 들어있는 정수의 개수 출력 
# - 6: 덱이 비어있으면 -1, 아니면 0 출력
# - 7 : 덱에 정수가 있다면 맨 앞의 정수 출력, 없다면 -1 출력
# - 8 : 덱에 정수가 있다면 맨 뒤의 정수 출력, 없다면 -1 출력 

# ✅ 내 풀이 아이디어:
# - collections의 deque 모듈 사용 

import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()
for _ in range(N):
  inputs = sys.stdin.readline().split()
  comm = int(inputs[0])

  if comm == 1:
    deq.appendleft(int(inputs[1]))
  
  elif comm == 2:
    deq.append(int(inputs[1]))

  elif comm == 3:
    if deq:
      sys.stdout.write(str(deq.popleft()) + '\n')
    else:
      sys.stdout.write('-1\n')
    
  elif comm == 4:
    if deq:
      sys.stdout.write(str(deq.pop()) + '\n')
    else:
      sys.stdout.write('-1\n')
    
  elif comm == 5:
    sys.stdout.write(str(len(deq)) + '\n')

  elif comm == 6:
    if not deq:
      sys.stdout.write('1\n')
    else:
      sys.stdout.write('0\n')
    
  elif comm == 7:
    if deq:
      sys.stdout.write(str(deq[0]) + '\n')
    else:
      sys.stdout.write('-1\n')
  
  elif comm == 8:
    if deq:
      sys.stdout.write(str(deq[-1]) + '\n')
    else:
      sys.stdout.write('-1\n')