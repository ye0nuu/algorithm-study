# BOJ 11718번: 그대로 출력하기
# URL: https://www.acmicpc.net/problem/11718
# 분류: 구현, 문자열
# 난이도: 브론즈 3
# 풀이 시간: 3분

# ✅ 문제 설명 요약:
# 입력 받은 대로 출력

# ✅ 내 풀이 아이디어:
# - EOFError 발생으로 입력 종료
# - 예외 발생 전까지 계속 입력과 출력을 반복

while True:
  try:
    s = input()
    print(s)
  except EOFError:
    break