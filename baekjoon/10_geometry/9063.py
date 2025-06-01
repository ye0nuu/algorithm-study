# BOJ 9063번: 대지 
# URL: https://www.acmicpc.net/problem/9063
# 분류: 수학, 구현, 기하학
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 임씨의 이름이 새겨진 옥구슬의 위치 N개가 주어질 때, 임씨에게 돌아갈 대지의 넓이를 계산 
# 단, 옥구슬의 위치는 2차원 정수 좌표로 주어지고 옥구슬은 같은 위치에 여러개 발견될 수도 있으며, 
# x축의 양의 방향을 동쪽, y축의 양의 방향을 북쪽이라고 가정 

# ✅ 내 풀이 아이디어:
# - 모든 x값, y값을 저장하는 배열을 만들어 각각 입력받아 저장
# - 폭은 최대x값-최소x값, 높이는 최대y값-최소y값으로 구함
# - weight*height로 넓이 출력

N = int(input())

x = []
y = []

for _ in range(N):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

weight = max(x) - min(x)
height = max(y) - min(y)

print(weight * height)