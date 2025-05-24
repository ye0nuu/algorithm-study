# BOJ 24263번: 알고리즘 수업 - 알고리즘의 수행 시간 2 
# URL: https://www.acmicpc.net/problem/24263
# 분류: 구현, 시뮬레이션 
# 난이도: 브론즈 4
# 풀이 시간: 2분

# ✅ 문제 설명 요약:
# 입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행시간을 예제 출력과 같은 방식으로 출력 
# MenOfPassion(A[], n) {
#    sum <- 0;
#    for i <- 1 to n
#        sum <- sum + A[i]; # 코드1
#    return sum;
# }

# ✅ 내 풀이 아이디어:
# - 해당 알고리즘의 수행횟수는 n이 되고, 하나의 반복문으로 시간복잡도는 O(n)이 되어 다항식으로 나타내었을 경우의 최고차항의 차수는 1이 된다.

n = int(input())

print(n)
print(1)