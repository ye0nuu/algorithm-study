# BOJ 7785번: 회사에 있는 사람 
# URL: https://www.acmicpc.net/problem/7785
# 분류: 자료 구조, 해시를 사용한 집합과 맵, 집합과 맵 
# 난이도: 실버 5
# 풀이 시간: 30분

# ✅ 문제 설명 요약:
# 로그에는 어떤 사람이 회사에 들아왔는지, 나갔는지가 기록되어져 있다.
# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - n을 입력받고, 현재 회사에 있는 사람을 저장하는 current 집합 생성
# - 출입한 사람, 상태를 n번 입력받고 enter인 경우 current에 이름 추가,
# - leave인 경우 current에서 해당 사람을 지움.
# - 최종 저장된 current 집합을 내림차순으로 정렬하고 줄을 맞추어 출력 

n = int(input())

current = set()
for _ in range(n):
  name, log = input().split()

  if log == 'enter':
    current.add(name)
  elif log == 'leave':
    current.remove(name)

print('\n'.join(sorted(current, reverse=True)))