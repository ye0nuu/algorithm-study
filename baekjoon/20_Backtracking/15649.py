# BOJ 15649번: N과 M (1)
# URL: https://www.acmicpc.net/problem/15649
# 분류: 백트래킹 
# 난이도: 실버 3
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성 
# - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 

# ✅ 내 풀이 아이디어:
# - pick 백트래킹 함수 작성, select 배열을 인수로 받고 배열 길이가 M과 같아지면 배열을 공백으로 나눠 출력하고 return
# - 호출되면 1부터 N까지 반복하며 i가 select 배열에 없을 경우 select+[i]을 인수로 하여 다시 호출
# - N과 M을 입력받고 빈 배열 []을 인수로 하여 pick 함수 호출

def pick(select):
  if len(select) == M:
    print(*select)
    return
  for i in range(1, N+1):
    if i not in select:
      pick(select + [i])

N, M = map(int, input().split())
pick([])