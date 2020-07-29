from copy import deepcopy 
from itertools import permutations
import math

N, M, K = map(int, input().split())
orgin_A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]

# roatation 방향별 값 변경
def right_convert(arr, sx, sy, len):
    for _ in range(len):
        arr[sx][sy] = orgin_A[sx][sy+1] 
        sx, sy = sx, sy+1
    return 

def down_convert(arr, sx, sy, len):
    for _ in range(len):
        arr[sx][sy] = orgin_A[sx+1][sy] 
        sx, sy = sx+1, sy
    return 

def left_convert(arr, sx, sy, len):
    for _ in range(len):
        arr[sx][sy] = orgin_A[sx][sy-1] 
        sx, sy = sx, sy-1
    return

def up_convert(arr, sx, sy, len):
    for _ in range(len):
        arr[sx][sy] = orgin_A[sx-1][sy] 
        sx, sy = sx-1, sy
    return

# 지정 사각형 회전 
def rotate(arr):
    new_arr = deepcopy(arr)
    (r, c, s) = Q
    # 파이썬 배열 
    r, c = r-1, c-1

    # 회전 사각형 극점 
    sx, sy = r-s, c-s
    ex, ey = r+s, c+s 
    # 회전 사각형의 중심 
    cx, cy = sx + (ex-sx)/2
    for i in range(cx-sx):
        # 한 라운드 마다 2만큼 길이의 이동(회전 사각형 한변의 길이)
        right_convert(new_arr, sx,sy, 2*i)
        down_convert(new_arr, sx,sy, 2*i)
        left_convert(new_arr, sx,sy, 2*i)
        up_convert(new_arr, sx,sy, 2*i)
    # 회전된 사각형이 반환
    return new_arr

# 행별 합의 최소값 구하기 
def min(arr):
    return min([sum(y) for y in arr])

# 최종 함수 
# 무한대로 큰값 설정
ans = math.inf
# Query 순서 조합
for q in [permutations(Q, K)]:
    new_arr = rotate(orgin_A)
    ans = min(ans, min(new_arr))

print(ans)
