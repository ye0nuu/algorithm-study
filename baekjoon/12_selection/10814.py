# BOJ 10814번: 나이순 정렬 
# URL: https://www.acmicpc.net/problem/10814
# 분류: 정렬
# 난이도: 실버 5
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - N을 입력받고 가입 정보를 입력받을 member 배열을 생성한다.
# - 나이와 이름을 입력받아 순서와 함께 member 배열에 배열형태로 추가한다. (2차원 배열)
# - lambda 함수로 나이를 기준으로 정렬하고, 같을 경우 가입순서 기준으로 정렬하도록 설정한다.
# - 형식에 맞게 출력한다.

N = int(input())

member = []
for i in range(N):
  age, name = input().split()
  member.append([i, int(age), name])

member.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
  print(f"{member[i][1]} {member[i][2]}")