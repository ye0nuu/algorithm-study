# BOJ 14889번: 스타트와 링크 
# URL: https://www.acmicpc.net/problem/14889
# 분류: 브루트포스 알고리즘, 백트래킹 
# 난이도: 실버 1
# 풀이 시간: 30분 

# ✅ 문제 설명 요약:
# 총 N명의 사람들을 N/2명으로 이루어진 스타트팀과 링크팀으로 나눠야 한다. (N은 짝수)
# 사람에게 번호를 1부터 N까지로 배정했고, 능력치를 조사했다. 능력치 S_ij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 S_ij의 합이다. S_ij는 S_ji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S_ij와 S_ji다.
# 두 팀의 능력치 차이를 최소로 하려고 할 때, 능력치 차이의 최솟값 출력 

# ✅ 내 풀이 아이디어:
# - N과 리스트 S를 입력받고, start 팀으로 뽑은 사람을 저장하는 visited 리스트를 False로 초기화하고 능력치 차이를 저장할 gap 변수를 큰 수로 초기화해 생성한다.
# - 백트래킹을 진행할 start_link 함수를 작성, 현재 뽑은 사람 수인 pick, 현재 고를 수 있는 사람 번호인 start를 인수로 받는다.
# - gap을 전역변수로 선언하고, pick이 N//2가 되어 팀을 다 뽑게 되면, 두 팀에 대해 모든 i와 j 쌍의 시너지를 합산한다.
# - i번째 사람과 j번째 사람이 모두 visited 배열 내에 있으면 둘 다 스타트 팀이므로 스타트팀 점수를 저장하는 A 변수에 합산하고, 둘다 배열 내에 없다면 링크팀인것이므로 B 변수에 합산한다.
# - A와 B 차이의 절댓값과 gap 중 작은 것을 gap에 저장하고 return
# - start부터 N까지 visited 배열 내에 해당 수(사람)가 없으면 뽑고(visited[i]를 True로) pick+1, i+1을 인수로 하여 start_link 함수를 호출한다.
# - 호출이 끝난 후 visited[i]를 False로 하여 되돌아간다. (백트래킹)
# - 본 코드에서 start_link(0, 0)을 호출해 gap 값을 구하고 출력한다.

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False for _ in range(N)]
gap = int(1e9)


def start_link(pick, start):
  global gap

  if pick == N // 2:
    A = 0
    B = 0
    for i in range(N):
      for j in range(N):
        if visited[i] and visited[j]:
          A += S[i][j]
        elif not visited[i] and not visited[j]:
          B += S[i][j]
    gap = min(gap, abs(A-B))
    return
  
  for i in range(start, N):
    if not visited[i]:
      visited[i] = True
      start_link(pick+1, i+1)
      visited[i] = False

start_link(0, 0)
print(gap)