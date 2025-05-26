# BOJ 1018번: 체스판 다시 칠하기 
# URL: https://www.acmicpc.net/problem/1018
# 분류: 구현, 브루트포스 알고리즘 
# 난이도: 실버 4 
# 풀이 시간: 30분

# ✅ 문제 설명 요약:
# MxN 크기의 보드를 잘라 8x8 크기의 체스판으로 만드려 함.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 하므로 보드를 잘라낸 후 몇 개의 정사각형을 다시 칠하려 함
# 8x8 크기는 아무데서나 골라도 될 때 다시 칠해야 하는 정사각형의 최소 개수를 구함.

# ✅ 내 풀이 아이디어:
# - N, M, 보드를 입력받고 min_count 변수를 최댓값으로 설정 
# - 보드 내 가능한 8*8 체스판의 경우를 2중반복문으로 탐색 
# - 체스판은 W, B로 시작하는 경우가 있으므로 두 경우를 모두 count 
# - 8*8 체스판을 이중반복문으로 순회하며
# - 체스판 기준 (x+y) 값이 짝수라면 시작 색과 같은 색이 나와야 하는데, 다른 색이 나오는 경우 각각의 경우에 count
# - 홀수라면 다른 색이 나와야 하는데, 같은 색이 나온다면 각각의 경우 count 
# - min_count, count1, count2 중 가장 작은 값을 다시 min_count에 저장 
# - 최종 저장된 min_count 값을 출력 

N, M = map(int, input().split())

board = []
for _ in range(N):
  board.append(input())

min_count = N * M

for i in range(N-7):
  for j in range(M-7):
      count1 = 0  # 'W' 시작인 경우 
      count2 = 0  # 'B' 시작인 경우

      for x in range(8):
        for y in range(8):
          check = board[i + x][j + y] # 현재 위치 

          if (x+y)%2 == 0:  # 시작 기준 색이 나와야 할 위치인 경우
            if check != 'W':   # W 시작인 경우
              count1 += 1      # W가 안 나오면 칠해야  
            if check != 'B':   # B 시작인 경우
              count2 += 1      # B가 안 나오면 칠해야 

          else:   # 시작 기준 색의 반대가 나와야 할 위치인 경우
            if check != 'B':
              count1 += 1
            if check != 'W':
              count2 += 1

      min_count = min(min_count, count1, count2)  # 경우의 수 중 가장 작은 수 고름 

print(min_count)