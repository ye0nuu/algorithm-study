# BOJ 25305번: 커트라인 
# URL: https://www.acmicpc.net/problem/25305
# 분류: 구현, 정렬
# 난이도: 브론즈 2
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# N명의 학생들이 응시한 시험에 점수가 가장 높은 k명이 상을 받는다면, 상을 받는 커트라인이 몇 점인지 구하라.
# 커트라인 - 상을 받는 사람들 중 점수가 가장 낮은 사람의 점수 

# ✅ 내 풀이 아이디어:
# - N, k를 입력받고 점수는 배열로 입력받음
# - 선택정렬로 배열 정렬
# - 오름차순으로 정렬되었으므로 N-k 인덱스가 커트라인이 됨.

N, k = map(int, input().split())

scores = list(map(int, input().split()))

for i in range(N):
  min_idx = i
  for j in range(i+1, N):
    if scores[j] < scores[min_idx]:
      min_idx = j
  scores[i], scores[min_idx] = scores[min_idx], scores[i]

print(scores[N-k])