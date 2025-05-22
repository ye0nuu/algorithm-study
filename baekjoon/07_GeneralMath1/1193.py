# BOJ 1193번: 분수찾기
# URL: https://www.acmicpc.net/problem/1193
# 분류: 수학, 구현 
# 난이도: 실버 5
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 배열에 분수가 적혀있음, 지그재그로 1, 2, 3 ...번
# X가 주어졌을 때 X번째 분수를 구하는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - layer는 대각선 기준 몇 번째 줄인지, count는 해당 인덱스의 위치 찾기 위한 변수
# - count+layer으로 X가 몇 번째 줄에 있는지 찾음
# - idx_layer에 해당 줄의 몇 번째 인덱스에 있는지 찾음
# - 짝수 번째 줄에서는 분자는 위->아래, 분모는 반대로 증가하므로 i는 감소시키고 j는 증가시킴
# - 홀수 번째 줄일 경우엔 반대로
# - 최종 구해진 분수 출력

X = int(input())

layer = 1
count = 0

while count + layer < X:
  count += layer
  layer += 1

idx_layer = X - count

if layer % 2 == 0:
  i = idx_layer
  j = layer - idx_layer + 1
else:
  i = layer - idx_layer + 1
  j = idx_layer

print(f"{i}/{j}")