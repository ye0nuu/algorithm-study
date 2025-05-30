# BOJ 1929번: 소수 구하기 
# URL: https://www.acmicpc.net/problem/1929
# 분류: 수학, 정수론, 소수 판정, 에라토스테네스의 체 
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성 

# ✅ 내 풀이 아이디어:
# - 에라토스테네스의 체를 이용해 범위 내의 모든 소수 구함
# - N까지의 수가 소수인지 저장하는 is_prime 배열을 True로 초기화
# - 0과 1은 포함되지 않으므로 False로 저장하고 시작
# - 2부터 루트N + 1까지의 수를 검사하며 is_prime이 True인 경우 i*i부터 N+1까지 i간격으로 i의 배수를 False 처리 
# - i*i부터 시작하는 이유는 그 전까지의 수는 이전에 이미 처리했기 때문
# - 소수만 True로 남은 is_prime 배열에서 M부터 N까지의 범위에서 True인 i출력 

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
  if is_prime[i]:
    for j in range(i*i, N+1, i):
      is_prime[j] = False

for i in range(M, N+1):
  if is_prime[i]:
    print(i)