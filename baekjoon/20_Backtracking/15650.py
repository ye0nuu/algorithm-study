# BOJ 15650번: N과 M (2)
# URL: https://www.acmicpc.net/problem/15650
# 분류: 백트래킹 
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성 
# - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 
# - 고른 수열은 오름차순이어야 한다.

# ✅ 내 풀이 아이디어:
# - 백트래킹 함수 pick을 작성, start와 select 배열을 인수로 받는다.
# - select 배열의 길이가 M이 되면 배열을 공백으로 나눠 출력하고 return
# - 함수가 호출되면 start부터 N까지 반복하며 해당 숫자가 select 배열에 없는지 검사해 pick 함수를 i+1, select+[i]를 인수로 하여 호출한다.
# - N, M을 입력받고 1과 빈 배열[]을 인수로 하여 pick 함수를 호출한다.

def pick(start, select):
  if len(select) == M:
    print(*select)
    return
  for i in range(start, N+1):
    if i not in select:
      pick(i+1, select + [i])

N, M = map(int, input().split())
pick(1, [])