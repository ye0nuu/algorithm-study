# BOJ 14888번: 연산자 끼워넣기  
# URL: https://www.acmicpc.net/problem/14888
# 분류: 브루트포스 알고리즘, 백트래킹 
# 난이도: 실버 1
# 풀이 시간: 30분 

# ✅ 문제 설명 요약:
# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
# 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈으로만 이루어져 있다.
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안된다.
# 식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - N과 A 리스트를 입력받고, 연산자를 각각 입력받는다.
# - 가장 큰 값과 가장 작은 값을 저장할 max_result, min_result 변수를 생성하고 각각 작은값, 큰값으로 초기화한다.
# - dfs 함수를 작성, 계산 위치를 저장할 idx, 현재 계산된 수를 저장하는 current, 연산자가 몇 개 남았는지 저장하는 add/sub/multi/div를 인수로 받는다.
# - max, min_result를 전역 변수로 선언한다.
# - idx 값이 N과 같아지면 max_result와 current 값중 큰 값을 max_result로 저장, min_result도 같은 과정 후 return
# - 다음 숫자를 저장할 next_num 변수를 A[idx] 값으로 해 생성한다.
# - 연산자 별로 0 이상일 경우 idx 값을 하나 증가시키고, current 값에 해당 연산자로 next_num을 계산한 뒤, 연산자 개수 값은 하나 감소시켜 dfs를 호출한다.
# - 모두 같은 과정을 진행하되, 나눗셈의 경우 음수 연산도 고려해야 하므로 current와 next_num의 곱셈값의 음/양수 경우로 나누어 연산한다.
# - idx는 1로, current는 A[0], 연산자는 입력값으로 하여 dfs를 최종호출하고 최종 저장된 max, min 값을 출력한다.

N = int(input())
A = list(map(int, input().split()))
add, sub, multi, div = (map(int, input().split()))

max_result = -int(1e9)
min_result = int(1e9)

def dfs(idx, current, add, sub, multi, div):
  global max_result, min_result

  if idx == N:
    max_result = max(max_result, current)
    min_result = min(min_result, current)
    return
  
  next_num = A[idx]

  if add > 0:
    dfs(idx+1, current + next_num, add - 1, sub, multi, div)
  if sub > 0:
    dfs(idx+1, current-next_num, add, sub-1, multi, div)
  if multi > 0:
    dfs(idx+1, current*next_num, add, sub, multi-1, div)
  if div > 0:
    if current * next_num < 0:
      dfs(idx+1, - (abs(current) // abs(next_num)), add, sub, multi, div-1)
    else:
      dfs(idx+1, current//next_num, add, sub, multi, div-1)

dfs(1, A[0], add, sub, multi, div)

print(max_result)
print(min_result)