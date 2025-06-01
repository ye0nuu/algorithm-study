# BOJ 2501번: 약수 구하기 
# URL: https://www.acmicpc.net/problem/2501
# 분류: 수학, 브루트포스 알고리즘
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수 출력

# ✅ 내 풀이 아이디어:
# - 약수를 저장하는 factors 배열을 만들고
# - 1부터 반복문을 돌며 해당 숫자가 약수일 경우 배열에 추가
# - 최종 약수 배열의 길이가 K보다 작으면 0을 출력하고, 아닌 경우 factors 배열의 K-1번째 숫자 출력

N, K = map(int, input().split())

factors = []
for i in range(1, N+1):
  if N%i == 0:
    factors.append(i)

if len(factors) < K:
  print(0)
else:
  print(factors[K-1])