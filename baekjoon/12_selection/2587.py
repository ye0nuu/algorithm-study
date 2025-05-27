# BOJ 2587번: 대표값2
# URL: https://www.acmicpc.net/problem/2587
# 분류: 수학, 구현, 정렬, 사칙연산 
# 난이도: 브론즈 2
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 다섯 개의 자연수가 주어질 때, 이들의 평균과 중앙값을 구하는 프로그램 작성 

# ✅ 내 풀이 아이디어:
# - 다섯 개의 숫자를 배열로 입력받음 
# - 선택정렬로 숫자 정렬, 5번 반복하면서 앞에서 뒤로 가며 가장 작은 원소를 맨앞으로 옮김
# - sum() 함수를 통해 평균값을 계산하고, 배열의 3번째 인덱스를 출력해 중앙값 구함 

num = []
for _ in range(5):
  num.append(int(input()))

for i in range(5):
  min_idx = i
  for j in range(i+1, 5):
    if num[j] < num[min_idx]:
      min_idx = j
  num[i], num[min_idx] = num[min_idx], num[i]

print(sum(num)//5)  # 평균 
print(num[2]) # 중앙값 