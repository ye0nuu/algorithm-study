# BOJ 3009번: 네 번째 점 
# URL: https://www.acmicpc.net/problem/3009
# 분류: 구현, 기하학
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - 찾으려는 각 x, y값은 주어진 모든 각 x, y값에서 같은 두 좌표와 다른 하나의 값과 같은 값이 될 것임 
# - if문으로 다른 하나의 값을 찾아내 저장하고 출력 

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
  x4 = x3
elif x1 == x3:
  x4 = x2
elif x2 == x3:
  x4 = x1

if y1 == y2:
  y4 = y3
elif y1 == y3:
  y4 = y2
elif y2 == y3:
  y4 = y1

print(f"{x4} {y4}")