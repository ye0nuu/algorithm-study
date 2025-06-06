# BOJ 20920번: 영단어 암기는 괴로워  
# URL: https://www.acmicpc.net/problem/20920
# 분류: 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵 
# 난이도: 실버 3
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 만들고자 하는 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용하여 만들어진다.
# 1. 자주 나오는 단어일 수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
# M보다 짧은 길이의 단어의 경우 읽는 것만으로 외울 수 있기 때문에 길이가 M이상인 단어들만 외운다.

# ✅ 내 풀이 아이디어:
# - N, M을 입력받고 단어와 빈도수를 저장할 dict 딕셔너리를 생성한다.
# - N개의 문자열을 입력받고, 길이가 M 이상일 경우 문자열이 dict 안에 있는지 검사
# - 있다면 value값을 +1하고, 없다면 문자열을 key로 가지고 value가 1인 인덱스 추가
# - 저장된 딕셔너리를 lambda함수와 sorted 함수 이용해 빈도수, 길이, 사전순으로 정렬 
# - 정렬된 사전을 형식에 맞춰 출력 

import sys

N, M = map(int, sys.stdin.readline().split())

dict = {}
for _ in range(N):
  s = sys.stdin.readline().strip()

  if len(s) >= M:
    if s in dict:
      dict[s] += 1
    else:
      dict[s] = 1
  
sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_dict:
  sys.stdout.write(word + '\n')