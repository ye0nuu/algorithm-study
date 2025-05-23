# BOJ 5073번: 삼각형과 세 변 
# URL: https://www.acmicpc.net/problem/5073
# 분류: 수학, 구현, 기하학
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의
# -> Equilateral: 세 변의 길이가 모두 같은 경우
# -> Isosceles: 두 변의 길이만 같은 경우
# -> Scelene: 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우 Invalid 출력
# 세 변의 길이가 주어질 때 위 정의에 따른 결과 출력 

# ✅ 내 풀이 아이디어:
# - 입력이 모두 0이 되기 전까지 반복, 변의 길이는 리스트로 입력받음 
# - sum(s)-max(s)로 가장 긴 변을 제외한 나머지 두 변의 길이를 구해 긴 변보다 작거나 같을 경우 Invlaid 출력
# - 모든 변의 길이가 같을 경우 Equilateral 출력
# - 두 변의 길이만 같을 경우 Isosceles 출력
# - 삼각형이지만 세 변의 길이가 모두 다른 경우 Scelene 출력 

while True:
  s = list(map(int, input().split()))
  if s[0] == s[1] == s[2] == 0:
    break

  if sum(s)-max(s) <= max(s):
    print("Invalid")
  elif s[0] == s[1] == s[2]:
    print("Equilateral")
  elif s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
    print("Isosceles")
  else:
    print("Scalene")