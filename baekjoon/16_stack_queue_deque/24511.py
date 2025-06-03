# BOJ 24511번: queuestack
# URL: https://www.acmicpc.net/problem/24511
# 분류: 자료 구조, 스택, 덱, 큐  
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# queuestack을 만들었다. 구조는 1, 2, .., N번의 자료구조(queue or stack)가 나열되어 있으며, 각 자료구조에는 한 개의 원소가 들어있다.
# 작동은 다음과 같다.
# - x0을 입력받는다.
# - x0을 1번 자료구조에 삽입한 뒤 1번 자료구조에서 원소를 pop, 그때 pop된 원소를 x1이라 한다.
# - x1을 2번 자료구조에 삽입한 뒤 2번 자료구조에서 원소를 pop, 그때 pop된 원소를 x2이라 한다. ...
# - x(n-1)을 N번 자료구조에 삽입한 뒤 N번 자료구조에서 원소를 pop, 그때 pop된 원소를 xN이라 한다.
# - xN을 리턴한다.
# 길이 M의 수열 C를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아있다.
# queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 스택에 원소를 넣었다 빼는 것은 무의미, 무시하고 큐인 자료구조(0)의 B[i] 값만 사용
# - 처음 A 배열에서 큐인 위치의 원소만 저장해 역순으로 qs 덱에 저장
# - 다음 C 배열을 순회하며 원소를 qs에 추가하고 앞에서 원소 pop(queue이므로) 반환되는 N 찾아 출력함 
# - !문제해결에 어려움 겪어 구글링 후 이해하는 방식 사용 -> 최적화 어려움 

import sys
from collections import deque

N = int(sys.stdin.readline()) 
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

qs = deque()
for i in range(N):
  if A[i] == 0:
    qs.appendleft(B[i])

for i in range(M):
  qs.append(C[i])
  print(qs.popleft(), end=' ')