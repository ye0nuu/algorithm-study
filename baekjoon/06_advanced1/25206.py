# BOJ 25206번: 너의 평점은
# URL: https://www.acmicpc.net/problem/25206
# 분류: 수학, 구현, 문자열
# 난이도: 실버 5
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 전공 평점을 계산해주는 프로그램 작성

# ✅ 내 풀이 아이디어:
# - 과목평점을 변환하기 위해 grade 딕셔너리 생성
# - 20개의 전공과목 입력받고 공백으로 분리해 리스트 생성
# - 과목 순회하며 과목평점이 P가 아닐 경우 누적 학점, 전공과목 성적 계산해 누적
# - 누적 성적/총 학점 계산해 전공평점 출력

grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
s = []
credit = 0.0
score = 0.0

for i in range(20):
  s.append(input().split())

for i in s:
  if i[2] != 'P':
    credit += float(i[1])
    score += grade[i[2]] * float(i[1])
  
print(score/credit)