# BOJ 14425번: 문자열 집합 
# URL: https://www.acmicpc.net/problem/14425
# 분류: 자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵 
# 난이도: 실버 4
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 총 N개의 문자열로 이루어진 집합 S가 있다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성 

# ✅ 내 풀이 아이디어:
# - 입출력 속도를 높이기 위해 sys 사용
# - N, M 입력받고 집합S 생성 후 입력받은 N개의 문자열을 집합에 추가
# - M개의 문자열을 입력받으며 집합 내에 있는 문자열인지 확인 후, 있을 경우 count
# - 최종 저장된 count값 출력 -> sys에서는 문자만 출력 가능하므로 str로 변환 후 출력

import sys

N, M = map(int, sys.stdin.readline().split())

S = set()
for _ in range(N):
  S.add(sys.stdin.readline().rstrip())

count = 0
for _ in range(M):
  st = sys.stdin.readline().rstrip()
  if st in S:
    count += 1

sys.stdout.write(str(count))