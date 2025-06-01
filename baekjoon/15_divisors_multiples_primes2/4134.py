# BOJ 4134번: 다음 소수 
# URL: https://www.acmicpc.net/problem/4134
# 분류: 수학, 브루트포스 알고리즘, 정수론, 소수 판정  
# 난이도: 실버 4
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 정수 n이 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수를 찾음 

# ✅ 내 풀이 아이디어:
# - 소수를 판별하는 is_prime 함수를 작성하여 소수이면 True 아니라면 False를 반환하게 하였다.
# - sys 모듈로 입출력 속도를 높였다.
# - 테스트 케이스의 수만큼 반복하며 n을 입력받고, 이보다 크거나 작은 소수를 찾는다.
# - is_prime이 False를 반환하는 동안 n을 1씩 증가시킨다.
# - n이 소수가 되면 반복문을 빠져나와 n을 출력한다.

import sys

def is_prime(n):
  if n < 2:
    return False
  elif n > 2:
    for i in range(2, int(n**0.5)+1):
      if n%i == 0:
        return False
    return True
  else:
    return True

def main():
  T = int(sys.stdin.readline())

  for _ in range(T):
    n = int(sys.stdin.readline())

    while not is_prime(n):
      n += 1
    sys.stdout.write(str(n) + '\n')

if __name__ == '__main__':
  main()