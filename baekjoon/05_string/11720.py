# BOJ 11720번: 숫자의 합
# URL: https://www.acmicpc.net/problem/11720
# 분류: 수학, 구현, 문자열
# 난이도: 브론즈 4
# 풀이 시간: 2분

# 문제 설명 요약:
# 공백 없이 쓰인 N개의 숫자를 모두 합해서 출력

# 내 풀이 아이디어:
# - input()으로 숫자 개수 n, 숫자 입력받아서 정수로 변환 
# - n만큼 반복하며 /, % 연산으로 숫자 누적합 계산 

n = int(input())
num = int(input())

sum = 0
for i in range(n):
  sum += (num%10)
  num = num//10
print(sum)