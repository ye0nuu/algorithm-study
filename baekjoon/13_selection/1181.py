# BOJ 1181번: 단어 정렬 
# URL: https://www.acmicpc.net/problem/1181
# 분류: 문자열, 정렬
# 난이도: 실버 5
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램 작성 
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# ✅ 내 풀이 아이디어:
# - N을 입력받고, 단어를 입력받을 arr 배열을 만든다.
# - 문자열을 입력받아 숫자라면 pass하고, 문자열일 경우에만 문자열과 길이가 배열에 이미 저장되어 있는지 확인
# - 배열 내에 없다면 문자열과 문자열의 길이를 저장 (2차원 배열)
# - 길이를 기준으로 먼저 정렬하고, 같은 길이라면 사전순으로 정렬되게 lambda 함수 설정
# - 형식에 맞춰 문자열만 출력 

N = int(input())

arr = []
for _ in range(N):
  s = input()
  if s.isdigit():
    pass
  elif [s, len(s)] not in arr:
    arr.append([s, len(s)])

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(len(arr)):
  print(arr[i][0])