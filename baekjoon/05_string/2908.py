# BOJ 2908번: 상수 
# URL: https://www.acmicpc.net/problem/2908
# 분류: 수학, 구현
# 난이도: 브론즈 2
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 수를 거꾸로 읽는 상수가 주어진 세자리 두 수 중 고르는 큰 수 출력 

# ✅ 내 풀이 아이디어:
# - 공백 기준으로 입력받은 두 숫자 분리해 저장장
# - 문자열로 접근해 각각 숫자 뒤집기
# - 뒤집은 두 수 비교해 큰 수 출력

A, B = input().split()

revA = int(A[::-1])
revB = int(B[::-1])

if revA >= revB:
  print(revA)
else:
  print(revB)