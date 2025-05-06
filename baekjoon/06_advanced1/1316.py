# BOJ 1316번: 그룹 단어 체커
# URL: https://www.acmicpc.net/problem/1316
# 분류: 구현, 문자열
# 난이도: 실버 5
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 단어 n개를 입력으로 받아 그룹 단어의 개수 출력
# 그룹단어 : 단어에 존재하는 모든 문자에 대해, 각 문자가 연속해서 나타나는 경우

# ✅ 내 풀이 아이디어:
# - 단어 저장하는 배열 만들어 n개의 단어 입력받음
# - 각 단어의 문자 순회하며 이전 문자와 현재 위치 문자 비교해 다를 경우,
# - 등장한 문자를 저장하는 check 배열에 이미 있는지 확인
# - 없을 경우 check 배열에 추가, 있을 경우 그룹 단어가 아니므로 그룹단어 세는 변수 count에서 제외하고 break
# - 이전 위치 문자 새롭게 저장하고 계속 반복

n = int(input())

str = []
for i in range(n):
  str.append(input())

count = n
for s in str:
  check = []
  prev = ''

  for i in s:
    if prev != i:
      if i not in check:
        check.append(i)
      else:
        count -= 1
        break
    prev = i

print(count)