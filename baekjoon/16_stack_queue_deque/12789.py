# BOJ 12789번: 도키도키 간식드리미 
# URL: https://www.acmicpc.net/problem/12789
# 분류: 자료 구조, 스택 
# 난이도: 실버 3
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 사람들은 현재 1열로 줄을 서 있고, 맨 앞의 사람만 이동이 가능하다.
# 인규는 번호표 순서대로만 통과할 수 있는 라인을 만들어 두었다.
# 이 라인과 대기열의 맨 앞 사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간이 있다.
# 현재 대기열의 사람들은 이 공간으로는 올 수 있지만 반대는 불가능하다.
# 승환이 앞에 서있는 학생수 N과 승환이 앞에 서 있는 모든 학생들의 번호표 순서가 주어질 때, 승환이가 간식을 받을 수 있는지 구한다.

# ✅ 내 풀이 아이디어:
# - 번호표를 리스트 형태로 입력받고 순서를 기록하는 seq 변수, 임시 줄을 나타내는 stack을 생성
# - 줄을 검사하며 줄의 맨 앞이 번호와 같으면 맨 앞 인덱스를 pop하고 순서 +1
# - 그렇지 않고 stack이 비지 않았으며 스택 맨 뒤가 순서와 같으면 stack의 맨 뒤를 pop하고 순서 +1
# - 모두 아니면 줄의 맨 앞에서 pop하여 stack에 추가
# - 줄이 다 비면 스택을 검사 -> 스택의 맨 뒤가 순서와 같으면 stack 맨 뒤에서 pop하고 순서 +1
# - 스택 맨 뒤가 순서와 다르면 break
# - 최종 스택이 비었으면 간식을 받을 수 있다. Nice 출력, 스택이 비지 않았으면 Sad 출력 

N = int(input())
line = list(map(int, input().split()))

seq = 1
stack = []

while line:
  if line[0] == seq:
    line.pop(0)
    seq += 1
  elif stack and stack[-1] == seq:
    stack.pop()
    seq += 1
  else:
    stack.append(line.pop(0))

while stack:
  if stack[-1] == seq:
    stack.pop()
    seq += 1
  else:
    break

if not stack:
  print("Nice")
else:
  print("Sad")