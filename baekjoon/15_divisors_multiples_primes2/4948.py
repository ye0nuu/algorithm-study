# BOJ 4948번: 베르트랑 공준 
# URL: https://www.acmicpc.net/problem/4948
# 분류: 수학, 정수론, 소수 판정, 에라토스테네스의 체 
# 난이도: 실버 2
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 베르트랑 공준은 임의의 자연수 n에 대해, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다. 
# 자연수 n이 주어졌을 때, n보다 크고 2n보다 작거나 같은 소수의 개수를 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 계속 반복하며 n을 입력받고, 0인 경우에는 종료한다.
# - 에라토스테네스의 체를 이용해 2n까지의 소수를 구한다.
# - 2n+1 크기의 소수를 판별하기 위한 is_prime 배열을 만들고, 0과 1은 소수가 아니므로 제외하고 시작
# - 2부터 루트2n +1까지의 수를 검사하며, is_prime T의 i번째 인덱스에 True가 저장되어있을 경우 i*i인덱스부터의 i의 배수를 제외시킨다.
# - n+1부터 2n+1 인덱스를 돌며 소수(True)라고 저장된 인덱스의 수를 세어 출력한다. 

while True:
  n = int(input())
  if n == 0:
    break

  is_prime = [True] * (2*n + 1)
  is_prime[0] = is_prime[1] = False

  for i in range(2, int((2*n)**0.5) + 1):
    if is_prime[i]:
      for j in range(i*i, 2*n+1, i):
        is_prime[j] = False

  count = 0
  for i in range(n+1, 2*n+1):
    if is_prime[i]:
      count += 1
  print(count)