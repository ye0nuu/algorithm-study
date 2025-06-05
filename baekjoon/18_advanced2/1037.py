# BOJ 1037번: 약수 
# URL: https://www.acmicpc.net/problem/1037
# 분류: 수학, 정수론 
# 난이도: 브론즈 1
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 진짜 약수들을 배열로 입력받고, 진짜 약수 중 가장 작은 수와 큰 수를 곱하면 N이 되므로 min, max 함수를 이용해 N을 구해 출력한다. 

div_len = int(input())
div = list(map(int, input().split()))

if div_len == 1:
  print(div[0] ** 2)
else:
  print(min(div) * max(div))