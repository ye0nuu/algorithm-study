# BOJ 27433번: 팩토리얼 2
# URL: https://www.acmicpc.net/problem/27433
# 분류: 수학, 사칙연산 
# 난이도: 브론즈 5
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 0보다 크거나 같은 정수 N이 주어질 때, N!을 출력 

# ✅ 내 풀이 아이디어:
# - 재귀함수 factorial 작성, n이 0이나 1일 때 return 1 하는 종료조건 설정
# - 아니라면 n * factorial(n-1)로 재귀호출
# - main에서 N 입력받고 factorial(N) 호출해 결과 출력

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)
  
def main():
  N = int(input())

  print(factorial(N))

if __name__ == '__main__':
  main()