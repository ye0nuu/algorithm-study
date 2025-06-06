# BOJ 24060번: 알고리즘 수업 - 병합 정렬 1
# URL: https://www.acmicpc.net/problem/24060
# 분류: 구현, 정렬, 재귀  
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 
# 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K번째 저장되는 수를 구함 
# 의사코드가 주어진다.

# ✅ 내 풀이 아이디어:
# - 

count = 0
result = -1

def merge_sort(A, p, r, K):
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q, K)
    merge_sort(A, q+1, r, K)
    merge(A, p, q, r, K)

def merge(A, p, q, r, K):
  global count, result
  tmp = []
  i = p
  j = q + 1

  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp.append(A[i])
      i += 1
    else:
      tmp.append(A[j])
      j += 1

  while i <= q:
    tmp.append(A[i])
    i += 1

  while j <= r:
    tmp.append(A[j])
    j += 1

  for i in range(len(tmp)):
    A[p + i] = tmp[i]
    count += 1
    if count == K:
      result = tmp[i]

def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))

  merge_sort(A, 0, N-1, K)
  print(result if result != -1 else -1)

if __name__ == '__main__':
  main()