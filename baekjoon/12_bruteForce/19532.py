# BOJ 19532번: 수학은 비대면강의입니다 
# URL: https://www.acmicpc.net/problem/19532
# 분류: 수학, 브루트포스 알고리즘 
# 난이도: 브론즈 2
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# { ax + by = c, dx + ey = f } 의 연립방정식에서 x, y의 값을 계산해야 함.
# 정수 a, b, c, d, e, f가 주어질 때, 유일하게 존재하는 (x, y)값을 구함 

# ✅ 내 풀이 아이디어:
# - 가감법을 이용해 x와 y의 계수를 각각 맞추어 빼, 각각 x와 y만 남겨 값을 구함 

a, b, c, d, e, f = map(int, input().split())

x = (c * e - f * b) // (a * e - d * b)
y = (c * d - f * a) // (b * d - e * a)

print(f"{x} {y}")