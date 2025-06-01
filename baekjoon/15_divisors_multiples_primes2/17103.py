# BOJ 17103번: 골드바흐 파티션 
# URL: https://www.acmicpc.net/problem/17103
# 분류: 수학, 정수론, 소수 판정, 에라토스테네스의 체 
# 난이도: 실버 2
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 골드바흐의 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다.
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자.
# 두 소수의 순서만 다른 것은 같은 파티션이다.

# ✅ 내 풀이 아이디어:
# - N까지의 소수 set을 구하는 prime_list 함수를 만든다. (에라토스테네스의 체 사용)
# - T를 입력받고, T개의 N을 입력받아 리스트로 만든다.
# - N 리스트 중, 가장 큰 수를 기준으로 prime_list를 호출해 소수 set을 반환받는다.
# - N마다 소수 리스트를 순회하며 해당 소수가 N//2보다 큰 경우에는 순회를 종료하고,
# - 아닌 경우, N-소수가 소수set내에 있는 경우 count 한다.
# - N마다 저장된 최종 count를 출력한다.

import sys

def prime_list(n):
  is_prime = [True] * (n+1)
  is_prime[0] = is_prime[1] = False
  
  for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
      for j in range(i*i, n+1, i):
        is_prime[j] = False

  prime_list = set()
  for i in range(n+1):
    if is_prime[i]:
      prime_list.add(i)
  
  return prime_list


def main(): 
  T = int(sys.stdin.readline())

  N_list = []
  for _ in range(T):
    N_list.append(int(sys.stdin.readline()))
    
  prime = prime_list(max(N_list))

  for N in N_list:
    count = 0
    for i in sorted(prime):
      if i > N//2:
        break
      if N-i in prime:
        count += 1
    sys.stdout.write(str(count) + '\n')

if __name__ == '__main__':
  main()