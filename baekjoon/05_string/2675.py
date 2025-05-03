# BOJ 2675번: 문자열 반복
# URL: https://www.acmicpc.net/problem/2675
# 분류: 구현, 문자열
# 난이도: 브론즈 2
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 문자열 S를 입력받고, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력

# ✅ 내 풀이 아이디어:
# - 입력받은 테스트케이스 개수만큼 반복하며 R, S 입력받아 공백 기준으로 분리
# - 결과값 배열 만들고, S 순회하며 결과 배열에 R 개수만큼 알파벳 추가
# - join() 이용해 하나의 문자열로 만들어 출력

T = int(input())

for i in range(T):
  R, S = input().split()
  R = int(R)

  result = []
  for index in S:
    result.append(index * R)

  print("".join(result))