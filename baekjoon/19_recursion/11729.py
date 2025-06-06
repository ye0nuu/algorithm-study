# BOJ 11729번: 하노이 탑 이동 순서 
# URL: https://www.acmicpc.net/problem/11729
# 분류: 재귀 
# 난이도: 골드 5
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 세개의 장대가 있고 첫번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여있다.
# 각 원판은 반경이 큰 순서대로 쌓여있다. 규칙에 따라 첫번째 장대에서 세번째 장대로 옮기려 한다.
# 1. 한번에 한개의 원판만을 다른 탑으로 옮길 수 있다.
# 2. 쌓아놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력. 단, 이동 횟수는 최소가 되어야 함 

# ✅ 내 풀이 아이디어:
# - 재귀함수 hanoi를 작성한다. 매개변수는 이동 과정을 저장할 move 배열, 원반 갯수, 시작기둥, 목표기둥, 보조기둥이다.
# - n이 1이 되면 move 배열에 start, end를 리스트로 추가 후 return
# - 그 전에는 n-1개를 보조기둥으로 이동 -> 가장 큰 원반을 목표 기둥으로 -> n-1개를 목표 기둥으로 이동시키는 과정을 진행
# - N을 입력받고 move 배열 생성 후 hanoi 호출(move 배열, N, 1, 3, 2)
# - len(move)로 이동 횟수 출력 후 move 배열도 형식 맞춰 출력 

def hanoi(move, n, start, end, temp):
  if n == 1:
    move.append([start, end])
    return
  else:
    hanoi(move, n-1, start, temp, end)
    move.append([start, end])
    hanoi(move, n-1, temp, end, start)


N = int(input())
move = []
hanoi(move, N, 1, 3, 2)

print(len(move))
for i in move:
  print(i[0], i[1])