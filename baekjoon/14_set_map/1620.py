# BOJ 1620번: 나는야 포켓몬 마스터 이다솜 
# URL: https://www.acmicpc.net/problem/1620
# 분류: 자료 구조, 해시를 사용한 집합과 맵, 집합과 맵 
# 난이도: 실버 4
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 도감에 수록되어 있는 포켓몬의 개수 N과 맞춰야 하는 문제의 개수 M이 주어질 때,
# 문제가 알파벳으로 들어오면 포켓몬 번호를 출력하고, 숫자로만 들어오면 포켓몬 번호에 해당하는 문자 출력 

# ✅ 내 풀이 아이디어:
# - N과 M을 입력받고, pocketmon 배열을 생성해 N줄을 입력받아 추가한다.
# - 인덱스 값과 저장하기 위해 pocketmon_dict 딕셔너리를 생성하고, 인덱스와 값을 저장한다.
# - M번 문제를 입력받고, 입력받은 문자열이 숫자일 경우, pocketmon 배열에서 m-1번 인덱스의 값을 출력
# - 숫자가 아닐 경우, pocketmon_dict에서 문자열에 해당하는 인덱스번호 + 1을 출력한다.

N, M = map(int, input().split())

pocketmon = []
for _ in range(N):
  pocketmon.append(input())
pocketmon_dict = {value: idx for idx, value in enumerate(pocketmon)}

for _ in range(M):
  m = input()

  if m.isdigit():
    print(pocketmon[int(m)-1])
  else:
    print(pocketmon_dict[m]+1)