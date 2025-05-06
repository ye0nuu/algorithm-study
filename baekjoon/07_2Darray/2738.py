# BOJ 2738번: 행렬 덧셈
# URL: https://www.acmicpc.net/problem/2738
# 분류: 수학, 구현, 사칙연산
# 난이도: 브론즈 3
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# N*M 크기의 두 행렬 A, B가 주어졌을 때, 두 행렬을 더하는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - N, M 한줄에 입력받고 분리, map으로 int 변환
# - 두 array 생성하고 각각 입력받음 (분리하고 map으로 변환하는 방식, 줄마다 list로 변환)
# - array의 각 인덱스끼리 더하고 형식 맞추어 출력

N, M = map(int, input().split())
array1 = []
array2 = []

for _ in range(N):
  array1.append(list(map(int, input().split())))

for _ in range(N):
  array2.append(list(map(int, input().split())))

for i in range(N):
  for j in range(M):
    print((array1[i][j] + array2[i][j]), end=' ')
  print()