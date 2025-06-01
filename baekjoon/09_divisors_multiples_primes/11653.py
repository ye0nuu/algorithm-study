# BOJ 11653번: 소인수분해 
# URL: https://www.acmicpc.net/problem/11653
# 분류: 수학, 정수론, 소수 판정, 소인수분해 
# 난이도: 브론즈 1
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - 소수인지 판별하는 isPrime 함수 작성
# - 입력받은 N이 1이 아닌 경우 N이 소수가 아닌 동안 반복해 계산
# - 나눌 소수를 2부터 시작해 나누어 떨어질 경우, 해당 소수를 소인수 배열에 추가하고 N을 해당 소수로 나누어 저장
# - 나누어 떨어지지 않으면, 나눌 소수를 소수가 될 때까지 검사하며 증가시킴
# - 반복문을 벗어난 후에 마지막 소수가 된 N까지 배열에 추가
# - 소인수배열을 오름차순 정렬시킨 후 출력 

def isPrime(n):
  if n < 2:
    return False
  else:
    for i in range(2, int(n**0.5)+1):
      if n%i == 0:
        return False
    return True
  
def main():
  N = int(input())

  if N != 1:
    prime = 2
    prime_fac = []

    while isPrime(N) == False:
      if N%prime == 0:
        prime_fac.append(prime)
        N /= prime
      else:
        while True:
          prime += 1
          if isPrime(prime):
            break
    prime_fac.append(int(N))
    
    sorted(prime_fac)
    for i in prime_fac:
      print(i)

if __name__ == "__main__":
  main()