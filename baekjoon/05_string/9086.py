# BOJ 9086번: 문자열
# URL: https://www.acmicpc.net/problem/9086
# 분류: 구현, 문자열
# 난이도: 브론즈 5
# 풀이 시간: 1분

# ✅ 문제 설명 요약:
# 문자열을 입력, 문자열의 첫 글자와 마지막 글자를 출력

# ✅ 내 풀이 아이디어:
# - input()으로 테스트케이스 개수 입력받고 정수로 변환
# - T만큼 반복하면서 s 입력받음
# - 인덱스로 첫 글자, 마지막 글자 접근해 출력

T = int(input())
if 1<=T<=10:
  for i in range(T):
    s = input()
    print(s[0] + s[len(s)-1])