# BOJ 11005번: 진법 변환 2
# URL: https://www.acmicpc.net/problem/11005
# 분류: 수학, 구현
# 난이도: 브론즈 1
# 풀이 시간: 15분

# ✅ 문제 설명 요약:
# 10진법 수 N이 주어지면, 이 수를 B진법으로 바꿔 출력

# ✅ 내 풀이 아이디어:
# - N이 0이면 바로 0을 출력하고, 아니면
# - dec 배열을 만들어 N이 0보다 큰 동안 루프 돌며 변환해 값 저장
# - N을 B로 나눈 나머지가 10보다 작으면 문자로 변환해 배열에 추가 -> 문자로 변환하지 않아 계속 런타임 에러 발생하는 에러 있었음
# - 10보다 크면 알파벳으로 변환해 배열에 추가
# - N에 N을 B로 나눈 몫 저장
# - 최종 dec 배열을 reverse()로 뒤집고 join()으로 출력

N, B = map(int, input().split())

if N == 0:
  print(0)
else:
  dec = []
  while N > 0:
    re = N % B
    if re < 10:
      dec.append(str(re))
    else:
      dec.append(chr(re+55))
    N //= B

  dec.reverse()
  print("".join(dec))