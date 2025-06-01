# BOJ 2839번: 영화감독 숌 
# URL: https://www.acmicpc.net/problem/2839
# 분류: 수학, 다이나믹 프로그래밍, 그리디 알고리즘 
# 난이도: 실버 4
# 풀이 시간: 20분

# ✅ 문제 설명 요약:
# 설탕은 3kg, 5kg 봉지가 있고, 사탕가게에 설탕을 정확하게 Nkg을 배달해야 한다.
# 최대한 적은 봉지를 들고 가려 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구함 

# ✅ 내 풀이 아이디어:
# - 봉지 수를 저장하는 min_pac 변수의 초기값은 -1로 설정
# - N이 5보다 큰 경우 N을 5로 나눈 값을 count에 임시 저장하고 N은 5로 나눈 몫으로 저장
# - N이 3으로 나누어 떨어지면 count와 N을 3으로 나눈 몫을 더해 min_pac에 저장
# - 나누어 떨어지지 않으면, count를 하나 감소시키고 N에 다시 5를 더함.
# - 그런 다음 다시 N이 3으로 나누어 떨어지는지 검사하고, 이 과정을 count가 0이 되기 전까지 반복 
# - 반복 중, 검사 결과가 나누어 떨어진다면 min_pac에 count+N//3 저장하고 break 
# - 최종 저장된 min_pac 값 출력 

N = int(input())

min_pac = -1
count = 0

if N >= 5:
  count = N // 5
  N %= 5

if N % 3 == 0:
  min_pac = count + N // 3
else:
  while count > 0:
    count -= 1
    N += 5
    
    if N % 3 == 0:
      min_pac = count + N // 3
      break

print(min_pac)