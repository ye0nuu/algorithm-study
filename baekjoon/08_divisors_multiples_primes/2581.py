# BOJ 2581번: 소수 
# URL: https://www.acmicpc.net/problem/2581
# 분류: 수학, 정수론, 소수 판정 
# 난이도: 브론즈 2
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟갑을 찾는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - 소수인지 판별하는 isPrime 함수 작성
# - M과 N을 입력받고 해당 범위를 순회하며 isPrime 함수로 소수인지 판별, 소수일 경우 prime 배열에 추가
# - 만약 prime 배열에 저장된 소수가 없다면 -1 출력, 아니라면 sum(), min() 함수로 합과 최솟값 출력 

def isPrime(n):
  if n < 2:
    return False
  else:
    for i in range(2, int(n**0.5)+1):
      if n%i == 0:
        return False
    return True


def main():
  M = int(input())
  N = int(input())

  prime = []
  for n in range(M, N+1):
    if isPrime(n):
      prime.append(n)
    
  if len(prime) == 0:
    print(-1)
  else:
    print(sum(prime))
    print(min(prime))

if __name__ == "__main__":
  main()