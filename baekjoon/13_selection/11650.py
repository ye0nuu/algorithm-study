# BOJ 11650번: 좌표 정렬하기 
# URL: https://www.acmicpc.net/problem/11650
# 분류: 정렬
# 난이도: 실버 5
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력 

# ✅ 내 풀이 아이디어:
# - N을 입력받고, 좌표를 저장하기 위한 coor 배열을 만든다.
# - coor에 좌표를 2차원 배열로 입력받고, sort() 함수로 정렬하여 형식에 맞춰 출력한다. 

import sys

N = int(sys.stdin.readline())

coor = []
for _ in range(N):
  coor.append(list(map(int, sys.stdin.readline().split())))

coor.sort()

for i in range(N):
  sys.stdout.write(f"{coor[i][0]} {coor[i][1]}\n")