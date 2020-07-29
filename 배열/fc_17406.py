from copy import deepcopy 
# deepcopy: 배열 객체 복사할때 주소값과 값을 만들때 사용 

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 남서, 북동 방향

# 최대값 
ans = 10000

# 행의 합 중 최소값 반환 
def value(arr):
    return min([sum(y) for y in arr])

# 변환 
def convert(arr, qry):
    (r, c, s) = qry
    r, c = r-1, c-1 # 파이썬 인덱스 
    # 기존 배열을 새로운 값으로 생성 
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        # 출발지점 
        rr, cc = r-i, c+i # 계속 대각선으로 진행 
        # 한 대각선 멀어지면 2칸 뭅, 두 대각선 멀어지면 4칸 뭅
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr


def dfs(arr, qry):
    global ans
    # 쿼리를 다 처리했다 
    # 쿼리 체크 1로 
    if sum(qry) == K:
        # ans에 min값을 저장해라. 
        ans = min(ans, value(arr))
        return 
    # 쿼리 다 처리 안했을경우
    for i in range(K):
        if qry[i]:
            continue
        new_arr = convert(arr, Q[i])
        qry[i] = 1 # 쿼리 이미 했으니 
        dfs(new_arr, qry) 
        qry[i] = 0 # 쿼리 안했다고 가정하고 

dfs(A, [0 for i in range(K)])
print(ans)    