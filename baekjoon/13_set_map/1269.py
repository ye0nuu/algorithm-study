# BOJ 1269번: 대칭 차집합 
# URL: https://www.acmicpc.net/problem/1269
# 분류: 자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵  
# 난이도: 실버 4
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A, B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력 
# 두 집합 A, B가 있을 때, (A-B), (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

# ✅ 내 풀이 아이디어:
# - A, B의 길이를 입력받고, A와 B를 집합으로 입력받는다.
# - (A - B)와 (B - A)의 합집합의 길이를 출력한다. (len, | 이용)

a, b = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len((A - B) | (B - A)))