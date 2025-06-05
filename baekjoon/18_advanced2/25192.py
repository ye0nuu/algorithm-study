# BOJ 25192번: 인사성 밝은 곰곰이 
# URL: https://www.acmicpc.net/problem/25192
# 분류: 자료구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵 
# 난이도: 실버 4
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다.
# 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.
# 새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.
# 채팅 기록 중 곰곰티콘이 사용된 횟수를 구함 

# ✅ 내 풀이 아이디어:
# - 

N = int(input())

count = 0
greet = set()

for _ in range(N):
  enter = input()

  if enter == 'ENTER':
    count += len(greet)
    greet.clear()
  else:
    greet.add(enter)
count += len(greet)

print(count)