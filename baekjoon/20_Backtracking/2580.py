# BOJ 2580번: 스도쿠 
# URL: https://www.acmicpc.net/problem/2580
# 분류: 구현, 백트래킹 
# 난이도: 골드 4
# 풀이 시간: 60분 

# ✅ 문제 설명 요약:
# 스도쿠는 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여있다.
# 나머지 빈 칸을 채우는 방식은 다음과 같다.
# 1. 각각의 가로 줄과 세로 줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력 

# ✅ 내 풀이 아이디어:
# - 9x9 배열에 수를 입력받고, 0이 있는 위치만 따로 blanks에 저장한다.
# - 현재 칸에 넣을 수 있는 숫자를 구하는 get_candidates 함수를 작성, 현재 칸의 행/열을 r, c 인수로 받는다.
# - 1부터 9까지 가능하니까 possible 집합에 1~9를 넣고, 이미 쓰인 숫자를 저장할 used 집합을 생성한다.
# - br, bc에 3x3 사각형 시작 좌표를 구해 저장하고, 3x3 박스를 돌며 숫자들을 used set에 추가한다.
# - 마지막에 possible - used로 가능한 숫자에서 사용된 것을 제거해 return 한다.
# - 스도쿠를 해결하는 함수 sudoku를 작성, 채운 칸 수인 n을 인수로 받는다.
# - 만약 n이 blanks의 길이와 같아져 빈칸을 다 채웠다면 결과를 출력하고 프로그램을 종료한다.
# - r, c에 n번째 빈칸의 위치를 저장하고, get_candidates(r,c) 함수로 가능한 숫자들만 구해 탐색한다.
# - 입력받았던 보드판의 r, c 위치에 가능한 숫자를 넣고, sudoku(n+1)을 호출해 다음 빈칸으로 넘어간다.
# - 그 이후에는 해당 위치를 다시 0으로 설정해 원상복구한다.(백트래킹)
# - 본 코드에서 sudoku(0)을 호출해 결과가 출력될 수 있도록 한다.

import sys
SIZE = 9

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blanks = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]


def get_candidates(r, c):
  possible = set(range(1, 10))
  used = set()

  for i in range(SIZE):
    used.add(board[r][i])
    used.add(board[i][c])

  br, bc = r // 3 * 3, c // 3 * 3
  for i in range(3):
    for j in range(3):
      used.add(board[br+i][bc+j])

  return possible - used


def sudoku(n):
  if n == len(blanks):
    for i in board:
      print(*i)
    sys.exit(0)

  r, c = blanks[n]
  for num in get_candidates(r, c):
      board[r][c] = num
      sudoku(n + 1)
      board[r][c] = 0

sudoku(0)