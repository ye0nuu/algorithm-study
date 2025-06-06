# BOJ 26069번: 붙임성 좋은 총총이 
# URL: https://www.acmicpc.net/problem/26069
# 분류: 자료구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵 
# 난이도: 실버 4
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 사람들이 만난 기록이 시간 순서대로 N개 주어진다.
# 무지개 댄스를 추지 않고 있던 사람이 무지개 댄스를 추고 있던 사람을 만나게 되면, 만난 시점 이후로 무지개 댄스를 추게 된다.
# 기록이 시작되기 이전 무지개 댄스를 추고 있는 사람은 총총이 뿐이라고 할 때, 마지막 기록 이후 무지개 댄스를 추는 사람이 몇 명인지 구함 

# ✅ 내 풀이 아이디어:
# - N만큼 반복하며, 'ChongChong'을 원소로 가진 dance 집합을 생성한다.
# - A, B를 입력받고 A가 dance 집합 내에 있을 경우, B를 집합에 추가하고 B가 집합 내에 있을 경우 집합에 A를 추가한다.
# - 반복문을 벗어난 후의 dance 집합 길이를 출력한다. 

N = int(input())

dance = set(['ChongChong'])
for _ in range(N):
  A, B = input().split()
  
  if A in dance:
    dance.add(B)
  elif B in dance:
    dance.add(A)

print(len(dance))