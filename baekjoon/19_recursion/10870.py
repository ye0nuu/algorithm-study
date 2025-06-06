# BOJ 10870번: 피보나치 수 5
# URL: https://www.acmicpc.net/problem/10870
# 분류: 수학, 구현  
# 난이도: 브론즈 5
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째부터는 바로 앞 두 피보나치 수의 합이 된다.
# -> Fn = Fn-1 + Fn-2 (n >= 2)
# n이 주어졌을 때, n번째 피보나치 수를 구함 

# ✅ 내 풀이 아이디어:
# - 재귀함수 fib 작성, n이 0이면 0 리턴, 1이면 1 리턴해 종료조건 만들고
# - 0과 1이 아닐 경우엔 fib(n-1) + fib(n-2)로 재귀호출
# - n입력받고 fib(n) 호출해 피보나치수 구해 출력 

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)
  
def main():
  n = int(input())

  print(fib(n))

if __name__ == '__main__':
  main()