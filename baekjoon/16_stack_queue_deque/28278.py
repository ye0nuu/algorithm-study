# BOJ 28278번: 스택 2 
# URL: https://www.acmicpc.net/problem/28278
# 분류: 자료 구조, 스택 
# 난이도: 실버 4
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성
# 1 X: 정수 X를 스택에 넣는다.
# 2 : 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력
# 3 : 스택에 들어있는 정수의 개수를 출력한다.
# 4 : 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5 : 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다. 

# ✅ 내 풀이 아이디어:
# - stack 배열을 만들고 N만큼 반복하며 입력을 받는다. 입력값이 두개인 경우를 위해 배열로 입력받고, 첫번째 값을 명령어로 저장한다.
# - 명령어가 1인 경우: stack에 두번째 입력값을 저장
# - 명령어가 2인 경우: 스택 길이가 0이 아닌경우(비지 않은 경우), pop()으로 맨위의 원소 빼어 출력 
# - 명령어가 3인 경우: 스택의 길이 출력
# - 명령어가 4인 경우: 스택 길이가 0이라면 빈스택이므로 1 출력, 아닌 경우 0 출력
# - 명령어가 5인 경우: 스택이 비지 않았다면 맨 마지막 원소 출력 

import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
  inputs = sys.stdin.readline().split()
  comm = int(inputs[0])

  if comm == 1:   # push 
    stack.append(int(inputs[1]))

  elif comm == 2: # pop
    if len(stack) != 0:
      sys.stdout.write(str(stack.pop()) + '\n')
    else:
      sys.stdout.write(str(-1) + '\n')

  elif comm == 3: # length
    sys.stdout.write(str(len(stack)) + '\n')

  elif comm == 4: # is_empty
    if len(stack) == 0:
      sys.stdout.write(str(1) + '\n')
    else:
      sys.stdout.write(str(0) + '\n')

  elif comm == 5: # peek
    if len(stack) != 0:
      sys.stdout.write(str(stack[-1]) + '\n')
    else:
      sys.stdout.write(str(-1) + '\n')