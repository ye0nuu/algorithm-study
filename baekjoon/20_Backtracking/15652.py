# BOJ 15652번: N과 M (4)
# URL: https://www.acmicpc.net/problem/15652
# 분류: 백트래킹 
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성 
# - 1부터 N까지 자연수 중에서 M개를 고른 수열 
# - 같은 수를 여러 번 골라도 된다.
# - 고른 수열은 비내림차순이어야 한다.
# - 길이가 K인 수열 A가 A1 <= A2 <= ... <= Ak-1 <= Ak 를 만족하면, 비내림차순이라고 한다. 

# ✅ 내 풀이 아이디어:
# - 백트래킹 함수 pick을 작성, 시작지점 start와 select 배열을 인수로 받는다.
# - select 배열의 길이가 M이 되면 공백으로 나눠 출력하고 return
# - start부터 N까지의 수를 반복하며, i와 select + [i]를 인수로 하여 pick 함수 계속해 호출
# - N과 M을 입력받고 1과 빈 배열 []을 인수로 하여 pick 함수 호출 

def pick(start, select):
  if len(select) == M:
    print(*select)
    return
  for i in range(start, N+1):
    pick(i, select + [i])

N, M = map(int, input().split())
pick(1, [])