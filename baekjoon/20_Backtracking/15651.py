# BOJ 15651번: N과 M (3)
# URL: https://www.acmicpc.net/problem/15651
# 분류: 백트래킹 
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성 
# - 1부터 N까지 자연수 중에서 M개를 고른 수열 
# - 같은 수를 여러 번 골라도 된다.

# ✅ 내 풀이 아이디어:
# - 백트래킹 함수 pick을 작성, 수열을 저장하기 위한 select 배열을 인수로 받는다.
# - select 배열 길이가 M이 되면 공백으로 나눠 출력하고 return
# - 1부터 N까지의 수를 반복하며 select + [i]를 인수로 하여 pick 함수를 계속해 호출한다.
# - N과 M을 입력받고 빈 배열 []을 인수로 하여 pick 함수를 호출한다.

def pick(select):
  if len(select) == M:
    print(*select)
    return
  for i in range(1, N+1):
    pick(select + [i])

N, M = map(int, input().split())
pick([])