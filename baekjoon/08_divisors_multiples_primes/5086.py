# BOJ 5086번: 배수와 약수
# URL: https://www.acmicpc.net/problem/5086
# 분류: 수학, 사칙연산 
# 난이도: 브론즈 3
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 두 수가 주어졌을 때, 다음 세 가지 중 어떤 관계인지 구함
# 1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

# ✅ 내 풀이 아이디어:
# - 반복문을 계속해서 돌며 0 0이 입력될 경우 종료
# - 두번째 숫자를 첫번째 숫자로 나누었을 때 나누어 떨어지면 약수라는 의미이므로 factor 출력
# - 첫번째 숫자를 두번째 숫자로 나누었을 때 나누어 떨어지면 약수라는 의미이므로 multiple 출력
# - 두가지 경우가 아니라면 neither 출력

while True:
  a, b = map(int, input().split())
  if a==0 and b==0:
    break

  if b % a == 0:
    print("factor")  
  elif a % b == 0:
    print("multiple")
  else:
    print("neither")