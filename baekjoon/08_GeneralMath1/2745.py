# BOJ 2745번: 진법 변환
# URL: https://www.acmicpc.net/problem/2745
# 분류: 수학, 구현, 문자열
# 난이도: 브론즈 2
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# B진법 수 N이 주어지면, 이 수를 10진법으로 바꿔 출력

# ✅ 내 풀이 아이디어:
# - 바꿀 수를 리스트 인덱스 거꾸로 순회하며 문자일 경우 숫자로 변환해 B진법 계산
# - 숫자일 경우 정수형으로 바꿔 B진법 계산 (pow() 함수 활용)
# - dec에 합을 누적해 최종 변환된 10진법 수인 dec 출력

B, N = input().split()

dec = 0
leng = len(B)

for i in range(leng):
  b = B[leng - i -1]
  if 'A' <= b <= 'Z':
    dec += (ord(b)-55) * pow(int(N), i)
  else:
    dec += int(b) * pow(int(N), i)

print(dec)