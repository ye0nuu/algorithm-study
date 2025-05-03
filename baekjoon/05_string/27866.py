# BOJ 27866번: 문자와 문자열
# URL: https://www.acmicpc.net/problem/27866
# 분류: 구현, 문자열
# 난이도: 브론즈 5
# 풀이 시간: 1분

# ✅ 문제 설명 요약:
# 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력

# ✅ 내 풀이 아이디어:
# - input()으로 단어와 정수를 입력받고
# - 문자열 인덱스로 접근

s = input()
i = int(input())
print(s[i-1])