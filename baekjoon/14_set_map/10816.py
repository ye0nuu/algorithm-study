# BOJ 10816번: 숫자 카드 2
# URL: https://www.acmicpc.net/problem/10816
# 분류: 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
# 난이도: 실버 4
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 상근이는 정수 하나가 적힌 숫자카드 N개를 갖고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 속도 개선을 위해 collections의 Counter와 sys 사용
# - N과 숫자카드 리스트를 입력받고, M과 숫자 리스트를 입력받음
# - Counter()를 이용해 cards 카드가 각각 몇개 있는지 구함
# - num을 순회하며 해당 숫자의 카드를 몇개 가지고 있는지 구해놓은 count 값을 가져와 새로운 result 배열에 저장
# - result 배열을 형식에 맞춰 출력 

from collections import Counter
import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

count = Counter(cards)

result = [str(count[n]) for n in num]
sys.stdout.write(" ".join(result))