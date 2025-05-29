# BOJ 1764번: 듣보잡 
# URL: https://www.acmicpc.net/problem/1764
# 분류: 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵 
# 난이도: 실버 4
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - N, M을 입력받고 사람들의 명단을 저장하기 위한 people 집합을 생성, 듣도보도 못한 사람들의 명단을 저장하기 위한 unknown 리스트 생성
# - 중복된 값이 나올 경우 듣도보도 못한 사람이 되므로 people 내에 이미 이름이 존재하면 unknown에 추가, 없다면 people 집합에 추가
# - unknown 배열의 길이를 구해 듣보잡의 수를 출력하고, 배열을 정렬하여 명단을 출력 

N, M = map(int, input().split())

people = set()
unknown = []
for _ in range(N+M):
  name = input()

  if name in people:
    unknown.append(name)
  else:
    people.add(name)

print(len(unknown))
print("\n".join(sorted(unknown)))