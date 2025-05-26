# BOJ 2750번: 수 정렬하기 
# URL: https://www.acmicpc.net/problem/2750
# 분류: 구현, 정렬 
# 난이도: 브론즈 2
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# ✅ 내 풀이 아이디어:
# - 버블정렬을 사용, 현재원소와 다음원소를 비교해 큰 수를 뒤로 옮김.
# - 이 과정을 한번 반복할 때마다 가장 큰 원소는 맨 뒤에 위치하게 됨 
# - 과정을 n-1번 반복하면 배열이 정렬 완료됨.
# - 정렬과정을 함수로 작성하여 사용하고, 정렬된 배열을 형식에 맞춰 출력 

def bubble_sort(A):
  n = len(A)

  for i in range(n-1):
    for j in range(0, n-i-1):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]

def main():
  N = int(input())

  num = []
  for _ in range(N):
    num.append(int(input()))

  bubble_sort(num)
  for i in num:
    print(i)

if __name__ == '__main__':
  main()