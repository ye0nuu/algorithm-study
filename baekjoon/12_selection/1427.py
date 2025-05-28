# BOJ 1427번: 소트인사이드 
# URL: https://www.acmicpc.net/problem/1427
# 분류: 문자열, 정렬
# 난이도: 실버 5
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자. 

# ✅ 내 풀이 아이디어:
# - N을 입력받고, 자릿수를 하나씩 나누어 저장할 배열을 만든다.
# - N이 0이 되기 전까지 배열에 N%10으로 끝자리 수를 추가하고, N//10으로 끝자리수를 뺀다. 
# - 저장된 배열을 sort(reverse=True)로 내림차순 정렬하고, join()을 통해 한줄로 출력한다. 

import sys

N = int(sys.stdin.readline())

arr = []
while N > 0:
  arr.append(N%10)
  N //= 10

arr.sort(reverse=True)
print(''.join(map(str, arr)))