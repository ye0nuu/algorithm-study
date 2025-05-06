# BOJ 2566번: 최댓값
# URL: https://www.acmicpc.net/problem/2566
# 분류: 구현
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 9x9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 최댓값을 찾고 최댓값이 몇행 몇열에 위치한 수인지 구하는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - 9x9 배열을 입력받음 (한 줄 입력받고 분리, map으로 정수 변환, 리스트로 변환하는 방식)
# - 배열 돌며 최대 수, 인덱스 위치 기록
# - 최종 최댓값과 위치 출력

num = []
for _ in range(9):
  num.append(list(map(int, input().split())))

max_num = 0
max_i = 0
max_j = 0
for i in range(9):
  for j in range(9):
    if num[i][j] >= max_num:
      max_num = num[i][j]
      max_i = i+1
      max_j = j+1

print(max_num)
print(max_i, max_j)