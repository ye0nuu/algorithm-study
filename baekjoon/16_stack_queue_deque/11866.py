# BOJ 11866번: 요세푸스 문제 0
# URL: https://www.acmicpc.net/problem/11866
# 분류: 구현, 자료구조, 큐 
# 난이도: 실버 4
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 1번부터 N번까지 N명의 사람이 원을 이루며 앉아있고, 양의 정수 K가 주어진다.
# 순서대로 K번째 사람을 제거한다. 한사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# N, K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성 

# ✅ 내 풀이 아이디어:
# - collections의 deque 모듈 사용
# - N, K를 입력받고 1부터 N까지의 수가 저장된 cir 배열 생성, 요세푸스 순열을 저장할 seq 배열 생성
# - cir 배열이 비기 전까지 반복하며 k 변수가 K와 같지 않을 경우 cir의 맨 앞의 요소를 빼 맨 뒤에 추가하고 k++
# - k가 K와 같아지면 cir의 맨 앞 요소를 빼어 seq 배열에 추가, k를 세기 위해 다시 1로 초기화
# - cir의 요소가 모두 없어지면 저장된 seq 배열 형식에 맞게 출력 

from collections import deque

N, K = map(int, input().split())

cir = deque([i for i in range(1, N+1)])
seq = []

k = 1
while cir:
  if k != K:
    cir.append(cir.popleft())
    k += 1
  else:
    seq.append(cir.popleft())
    k = 1

print("<" + ", ".join(map(str, seq)) + ">")