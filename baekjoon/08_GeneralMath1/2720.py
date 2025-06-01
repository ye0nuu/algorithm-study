# BOJ 2720번: 세탁소 사장 동혁
# URL: https://www.acmicpc.net/problem/2720
# 분류: 수학, 그리디 알고리즘, 사칙연산
# 난이도: 브론즈 3
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 거스름 돈의 액수가 주어지면 주어야 할 $0.25, $0.10, $0.05, $0.01의 개수를 구하는 프로그램 작성
# 거스름 돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 해야 함

# ✅ 내 풀이 아이디어:
# - T만큼 테스트케이스 반복
# - 센트 단위로 입력받으므로 입력받은 값을 25, 10, 5로 나누고 나머지를 저장해 거스름돈 구함

T = int(input())

for _ in range(T):
  c = int(input())

  quarter = c // 25
  c %= 25

  dime = c // 10
  c %= 10

  nickel = c // 5
  c %= 5

  penny = c

  print(quarter, dime, nickel, penny)
