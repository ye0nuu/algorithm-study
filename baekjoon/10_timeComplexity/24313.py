# BOJ 24313번: 알고리즘 수업 - 점근적 표기 1
# URL: https://www.acmicpc.net/problem/24313
# 분류: 수학
# 난이도: 실버 5 
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자.
# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# 함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.

# ✅ 내 풀이 아이디어:
# - bigO 성립을 위해서는 f(n)의 첫 차수의 계수가 c보다 작거나 커야함 
# - 그리고 f(n)<=cxg(n)을 만족해야하므로 a1 <= c and a1*n0+a0 <= c*n0을 만족하면 1 출력 

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

is_bigO = 0
if a1 <= c and a1*n0+a0 <= c*n0:
  is_bigO = 1

print(is_bigO)