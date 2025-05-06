# BOJ 1157번: 단어 공부
# URL: https://www.acmicpc.net/problem/1157
# 분류: 구현, 문자열
# 난이도: 브론즈 1
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내기
# 대소문자 구분 X

# ✅ 내 풀이 아이디어:
# - 입력받은 문자열을 대문자로 변환하고 알파벳 개수 세는 딕셔너리 생성
# - 문자열을 순회하며 해당 문자가 딕셔너리에 없으면 1을 저장해 인덱스 생성하고 있으면 값 +1
# - 딕셔너리 순회하며 값이 max_count보다 크면 max_count에 새로운 값을 저장하고 max_char에 key 저장
# - 값이 max_count와 같으면 max_char에 ? 저장
# - 최종 저장된 max_char값 출력

s = input().upper()

count = {}
for i in s:
  if i not in count:
    count[i] = 1
  else:
    count[i] += 1

max_char = '0'
max_count = -1

for i in count:
  if count[i] > max_count:
    max_count = count[i]
    max_char = i
  elif count[i] == max_count:
    max_char = '?'

print(max_char)