# BOJ 2231번: 분해합 
# URL: https://www.acmicpc.net/problem/2231
# 분류: 브루트포스 알고리즘 
# 난이도: 브론즈 2
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. (생성자가 없을 수도, 여러개일 수도 있음)
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 1부터 N까지 생성자를 찾아내는 과정 반복 
# - temp에 M 값을 임시저장하고 dec_sum에 분해합 저장
# - temp값이 0보다 크면 temp의 마지막 자릿수(temp%10)를 dec_sum에 더하고 temp의 마지막 자릿수 삭제(temp//10)하는 방식으로 자릿수까지 더함 
# - 구해진 분해합이 N과 같고 기존의 생성자보다 작은 경우 M값을 새로운 생성자 값으로 저장
# - 최종 저장된 con 값이 초기값과 같으면 생성자가 없는 경우이므로 0 출력, 아닐 경우 구한 생성자 값 출력 

N = int(input())

con = N   # 생성자
for M in range(1, N):
  temp = M
  dec_sum = temp   # 분해합 

  while temp > 0:
    dec_sum += (temp % 10)
    temp //= 10
  
  if dec_sum == N and M < con:
    con = M

if con == N:
  print(0)
else:
  print(con)