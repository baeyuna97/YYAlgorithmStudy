# 백준 1158 : 요세푸스 문제

# input
N, K = map(int, input().split())

# 사람 순서대로 정렬된 리스트 생성
people = list(range(1, N+1))

# 결과값 담을 객체
out_lst = []

while len(people) >= 3:
    # K번째 사람 제거 순서값에 추가
    out_lst.append(people[K-1])
    # K번째 사람 제거
    del people[K-1]

out_lst.append(people[0])
out_lst.append(people[1])

print('<'+','.join(map(str, out_lst)) + '>')