# BOJ 9184번: 신나는 함수 실행 
# URL: https://www.acmicpc.net/problem/9184
# 분류: 다이나믹 프로그래밍, 집합과 맵, 재귀 
# 난이도: 실버 2
# 풀이 시간: 15분 

# ✅ 문제 설명 요약:
# 주어진 재귀함수는 시간이 오래 걸린다. 이를 참고해 a, b, c가 주어졌을 때 빠르게 w(a, b, c)를 출력하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 중복호출을 저장하는 memo 딕셔너리 생성
# - 이전에 계산된 값이 memo에 있으면 바로 return해서 중복 계산 x
# - a, b, c 중 하나라도 0 이하이면 1을 저장하고 반환 
# - a<b<c일 때는 해당 알고리즘 규칙에 따라 계산해 저장하고 값 반환
# - 그 외에는 일반적인 규칙을 적용해 계산하고 값 메모에 저장, 반환
# - 본 코드에서는 계속해 반복하며 a, b, c를 입력받고 모두 -1일 경우에 종료
# - w(a, b, c)를 호출해 형식에 맞춰 값을 출력 

memo = {}
def w(a, b, c):
  if (a, b, c) in memo:
    return memo[(a, b, c)]
  
  if a<=0 or b<=0 or c<=0:
    memo[(a, b, c)] = 1
    return 1
  
  if a>20 or b>20 or c>20:
    memo[(a, b, c)] = w(20, 20, 20)
    return memo[(a, b, c)]
  
  if a<b and b<c:
    memo[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return memo[(a, b, c)]
  
  memo[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return memo[(a, b, c)]


while True:
  a, b, c = map(int, input().split())
  if a == b == c == -1:
    break

  print(f"w({a}, {b}, {c}) = {w(a, b, c)}")