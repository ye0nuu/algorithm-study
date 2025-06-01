# BOJ 9012번: 괄호 
# URL: https://www.acmicpc.net/problem/9012
# 분류: 자료 구조, 문자열, 스택 
# 난이도: 실버 4
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 '(', ')' 만으로 구성되어 있는 문자열이다.
# 그 중 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해 결과를 YES와 NO로 나타내어야 한다.

# ✅ 내 풀이 아이디어:
# - 테스트케이스 개수만큼 반복하며 괄호문자열을 입력받는다.
# - 스택을 하나 생성하고 괄호문자열을 순회하며 '('인 경우 스택에 추가
# - ')'인 경우, 빈스택이 아니면 pop(), 빈스택이면 (를 스택에 추가하고 break -> 이미 vps가 아님
# - 최종 스택에 아무것도 없을 경우 짝이 맞는 것이므로 YES 출력, 남은 게 있을 경우 짝이 안 맞는 것이므로 NO 출력 

import sys

T = int(sys.stdin.readline())

for _ in range(T):
  ps = sys.stdin.readline()

  stack = []
  for p in ps:
    if p == '(':
      stack.append(p)
    elif p == ')':
      if len(stack) != 0:
        stack.pop()
      else:
        stack.append(p)
        break

  if len(stack) == 0:
    sys.stdout.write('YES\n')
  else:
    sys.stdout.write('NO\n')