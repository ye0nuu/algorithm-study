# BOJ 10101번: 삼각형 외우기 
# URL: https://www.acmicpc.net/problem/10101
# 분류: 구현, 기하학
# 난이도: 브론즈 3
# 풀이 시간: 5분

# ✅ 문제 설명 요약:
# 삼각형의 세 각을 입력받아,
# -> 세 각의 크기가 모두 60이면, Equilateral
# -> 세 각의 합이 180이고, 두 각이 같은 경우에는 lsosceles
# -> 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# -> 세 각의 합이 180이 아닌 경우에는 Error 를 출력

# ✅ 내 풀이 아이디어:
# - 세 각 입력받아 합이 180이 아닐 경우 Error 출력,
# - 세 각이 모두 같은 경우 모두 60도이므로 Equilateral 출력
# - 세 각 중 두 각만 같은 경우 Isosceles 출력
# - 모두 아닌 경우, 세 각의 합이 180이지만 같은 각이 없으므로 Scalene 출력

an1 = int(input())
an2 = int(input())
an3 = int(input())

if an1+an2+an3 != 180:
  print("Error")
elif an1 == an2 == an3:
  print("Equilateral")
elif an1 == an2 or an1 == an3 or an2 == an3:
  print("Isosceles")
else:
  print("Scalene")