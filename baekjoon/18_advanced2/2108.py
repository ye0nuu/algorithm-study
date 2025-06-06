# BOJ 2108번: 통계학 
# URL: https://www.acmicpc.net/problem/2108
# 분류: 수학, 구현, 정렬, 집합과 맵 
# 난이도: 실버 2
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정 
# 1. 산술평균: N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값: N개의 수들 중 가장 많이 나타나는 값
# 4. 범위: N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통곗값을 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - N개의 숫자를 입력받아 arr 배열에 저장 후 sort() 함수 이용해 정렬
# - sum(arr) / N으로 평균 구한 후 round() 함수로 반올림 후 출력
# - N//2 인덱스 통해 배열의 중앙값 출력
# - 최빈값 구하기 위해 count 딕셔너리 생성하고 arr 배열 값 돌며 원소가 count에 있을 경우 키값을 원소로 하는 value값 +1
# - 없을 경우 원소를 키값, value를 1로 새 인덱스 추가
# - count 딕셔너리를 순회하며 딕셔너리의 value max값을 가지는 key만 mode 배열에 추가
# - mode 배열 정렬하고 길이가 1보다 큰 경우 두번째 인덱스값 출력하고, 1인경우 해당 원소 출력
# - arr 배열의 최댓값 - 최솟값으로 범위 구해 출력 
# - (최빈값 구하는 데 어려움 -> 딕셔너리, comprehension)

import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
  arr.append(int(sys.stdin.readline()))
arr.sort()

sys.stdout.write(str(round(sum(arr) / N)) + '\n')
sys.stdout.write(str(arr[N//2]) + '\n')

count = {}
for i in arr:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1

mode = [k for k, v in count.items() if v == max(count.values())]
mode.sort()
if len(mode) > 1:
  sys.stdout.write(str(mode[1]) + '\n')
else:
  sys.stdout.write(str(mode[0]) + '\n')

sys.stdout.write(str(max(arr) - min(arr)) + '\n')