# BOJ 9506번: 약수들의 합
# URL: https://www.acmicpc.net/problem/9506
# 분류: 수학, 구현, 정수론 
# 난이도: 브론즈 1
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# n이 완전수인지 아닌지 판단해주는 프로그램 작성
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

# ✅ 내 풀이 아이디어:
# - n을 입력받고 계속 반복문을 돌지만 -1이 들어오면 멈춤 
# - 약수를 저장하는 배열을 만들고 자신을 제외한 약수를 저장함
# - n과 구해진 약수들의 합이 같으면 n을 약수들의 합으로 나타내어 출력
# - 아니라면 양식에 맞추어 출력 

while True:
  n = int(input())
  if n == -1:
    break

  factors = []
  for i in range(1, n):
    if n%i == 0:
      factors.append(i)

  if n == sum(factors):
    print(f"{n} = {' + '.join(map(str, factors))}")
  else:
    print(f"{n} is NOT perfect.")