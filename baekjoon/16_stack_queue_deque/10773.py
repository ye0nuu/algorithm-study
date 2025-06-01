# BOJ 10773번: 제로 
# URL: https://www.acmicpc.net/problem/10773
# 분류: 자료 구조, 스택 
# 난이도: 실버 4
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 쓴 수를 지우게 됨
# 모든 수를 받아 적은 후, 그 수의 합 구함 

# ✅ 내 풀이 아이디어:
# - num 스택을 만들고 K번 반복하며 수를 입력받는다.
# - 수가 0이 아닐 경우 스택에 추가하고, 0일 경우 pop()으로 맨 위 수를 꺼내 지운다.
# - 최종 저장된 num스택의 합을 출력한다. 

import sys

K = int(sys.stdin.readline())

num = []
for _ in range(K):
  n = int(sys.stdin.readline())
  
  if n != 0:
    num.append(n)
  else:
    num.pop()
  
sys.stdout.write(str(sum(num)))