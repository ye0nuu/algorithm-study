# BOJ 9663번: N-Queen
# URL: https://www.acmicpc.net/problem/9663
# 분류: 브루트포스 알고리즘, 백트래킹 
# 난이도: 골드 4
# 풀이 시간: 60분

# ✅ 문제 설명 요약:
# N-Queen 문제는 크기가 NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성 

# ✅ 내 풀이 아이디어:
# - 백트래킹을 위한 queen 함수를 작성, 체스판 크기 n, 현재 행 row, 각 열의 정보를 저장하는 cols 리스트, 오른쪽 아래 대각선 불가능 여부를 저장하는 r_diag 리스트, 왼쪽 대각선 저장하는 l_diag 리스트를 인수로 한다.
# - 행을 탐색해 row가 n과 같아지면 경우의 수를 하나 증가시키는 의미로 1을 리턴 
# - 총 경우의 수를 저장하는 count 변수를 0으로 초기화
# - n만큼 반복하며 행별로 퀸을 놓을 수 있는 열의 위치(cols[])를 찾음. 이미 해당 열에 퀸이 있으면 x, 오른쪽 아래 대각선 공격이 가능하면 x(row-col+n-1 인덱스), 왼쪽 아래(row+col) 공격이 가능하면 x
# - 안되는 경우를 제외, 퀸을 놓은 위치를 true로 기록하고 queen 함수를 호출해 재귀를 통해 다음 행으로 이동(row+1)한다.
# - 재귀가 끝나면 다시 돌아가서 다음 열을 탐색한다. 호출 결과 누적된 경우의 수가 반환된다.
# - 본 코드에서 N을 입력받고 cols, r_diag, l_diag 배열을 False로 초기화 한다.
# - queen 함수를 호출하여 반환된 결과를 출력한다.

def queen(n, row, cols, r_diag, l_diag):
  if row == n:
    return 1
  
  count = 0
  for col in range(n):
    if cols[col] or r_diag[row - col + n - 1] or l_diag[row + col]:
      continue

    cols[col] = r_diag[row - col + n - 1] = l_diag[row + col] = True
    count += queen(n, row + 1, cols, r_diag, l_diag)
    cols[col] = r_diag[row - col + n - 1] = l_diag[row + col] = False
  return count


N = int(input())
cols = [False] * N
r_diag = [False] * (2 * N - 1)
l_diag = [False] * (2 * N - 1)

print(queen(N, 0, cols, r_diag, l_diag))