# BOJ 10989번: 수 정렬하기 3
# URL: https://www.acmicpc.net/problem/10989
# 분류: 정렬
# 난이도: 브론즈 1
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬 

# ✅ 내 풀이 아이디어:
# - sys로 입출력, 속도 높임
# - num배열을 최대 개수인 10001개만큼 0으로 초기화하고 수를 입력받아 해당 수의 인덱스에 +1(등장 횟수 기록)
# - 이러한 계수정렬 사용하고 배열을 순회하며 해당 인덱스의 값이 0이상이라면 값만큼 해당 인덱스값 출력 

import sys

N = int(sys.stdin.readline())

num = [0]*10001
for _ in range(N):
  n = int(sys.stdin.readline())
  num[n] += 1

for i in range(1, 10001):
    for _ in range(num[i]):
        sys.stdout.write(str(i) + '\n')