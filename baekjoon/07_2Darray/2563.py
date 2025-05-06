# BOJ 2563번: 색종이 
# URL: https://www.acmicpc.net/problem/2563
# 분류: 구현
# 난이도: 실버 5
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 가로세로 크기가 각각 100인 정사각형 도화지 위에, 가로세로 크기가 각각 10인 정사각형 색종이를 변끼리 평행하도록 붙임
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 영역의 넓이를 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 도화지 모양의 2차원 배열을 만들고 0으로 초기화
# - 도화지와 색종이 간의 거리를 입력받고 그 크기만큼 배열에 1을 지정
# - 최종 완성된 0과 1로 이루어진 배열에서 1을 세면 색종이 영역의 크기

n = int(input())

white = [[0] * 100 for _ in range(100)]

for _ in range(n):
  left, bottom = map(int, input().split())

  for i in range(left, left+10):
    for j in range(bottom, bottom+10):
      if i<100 and j<100:
        white[i][j] = 1

count = 0
for i in range(100):
  count += white[i].count(1)

print(count)