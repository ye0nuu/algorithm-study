# BOJ 18870번: 좌표 압축 
# URL: https://www.acmicpc.net/problem/18870
# 분류: 정렬, 값/좌표 압축 
# 난이도: 실버 2
# 풀이 시간: 30분

# ✅ 문제 설명 요약:
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi>Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자. 

# ✅ 내 풀이 아이디어:
# - N을 입력받고, 좌표들을 리스트로 입력받는다.
# - 좌표를 대응시켜 압축시키기 위해 집합으로 중복을 제거하고, 오름차순으로 정렬한다.
# - enumerate로 인덱스값과 값을 구해 딕셔너리로 저장
# - 리스트 컴프리헨션으로 기존 배열의 원소를 coor에서 찾아 압축값으로 바꾸어 다른 배열로 저장한다.
# - 형식에 맞춰 변환된 리스트 출력 

N = int(input())
arr = list(map(int, input().split()))

sorted_set = sorted(set(arr))
coor = {value: idx for idx, value in enumerate(sorted_set)}

com_arr = [coor[num] for num in arr]

print(" ".join(map(str, com_arr)))