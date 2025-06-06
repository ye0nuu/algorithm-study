# BOJ 25501번: 재귀의 귀재 
# URL: https://www.acmicpc.net/problem/25501
# 분류: 구현, 문자열, 재귀  
# 난이도: 브론즈 2
# 풀이 시간: 10분

# ✅ 문제 설명 요약:
# 팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다.
# 어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀함수로 쉽게 해결한다.
# 작성된 isPalindrome 함수를 이용해 문자열이 팰린드롬인지 여부를 확인하려 한다.
# 함수의 반환값과 recursion 함수의 호출 횟수를 구한다.

# ✅ 내 풀이 아이디어:
# - 문제의 함수를 수정해 작성 후 호출 횟수 구하기 위해 global 변수 count 생성
# - main에서 T번 반복하며 문자열 입력받고 count 0으로 초기화
# - recursion 함수 초반에 count +1을 해서 호출시마다 횟수 세도록 함 
# - isPalindrome 호출해 팰린드롬인지 여부와 count 통해 호출횟수 출력 

def recursion(s, l, r):
  global count
  count += 1

  if l >= r:
    return 1
  elif s[l] != s[r]:
    return 0
  else:
    return recursion(s, l+1, r-1)
  
def isPalindrome(s):
  return recursion(s, 0, len(s)-1)

def main():
  global count
  T = int(input())

  for _ in range(T):
    s = input()
    count = 0

    print(isPalindrome(s), count)

if __name__ == '__main__':
  main()