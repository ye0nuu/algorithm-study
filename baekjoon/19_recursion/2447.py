# BOJ 2447번: 별 찍기 - 10 
# URL: https://www.acmicpc.net/problem/2447
# 분류: 분할 정복, 재귀 
# 난이도: 골드 5
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 재귀적인 패턴으로 별을 찍어보자. N이 3의 거듭제곱이라고 할 때, 크기 N의 패턴은 NxN 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)x(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.

# ✅ 내 풀이 아이디어:
# - 별을 찍는 star 재귀함수 작성
# - n이 1이 되면 x와 y위치에 별 찍음
# - 전체 정사각형을 3x3의 정사각형으로 나누기 위해 size를 n//3으로 설정하고
# - 나눠진 정사각형의 각 칸을 돌며 가운데 칸은 지나치고, 나머지 칸에 대해 다시 star 함수 호출
# - 호출 시 좌표를 이동하기 위해 x+i*size, y+j*size를 x, y로 호출하고, size를 n으로 사용해 호출한다.
# - 별을 찍기 위해 N을 입력받고 NxN 크기의 빈 배열을 생성한다.
# - 0, 0 위치에서부터 시작하므로 star(0, 0, N) 호출해 배열 채움
# - 최종 저장된 stars 배열을 출력 

def star(x, y, n):
  if n == 1:
    stars[x][y] = '*'
    return

  size = n // 3
  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        continue
      star(x + i * size, y + j * size, size)


N = int(input())
stars = [[" " for _ in range(N)] for _ in range(N)]

star(0, 0, N)
for line in stars:
  print(''.join(line))