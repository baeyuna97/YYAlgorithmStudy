n, k = map(int, input().split())

tree = dict()
n_lst = list(range(n))

for i in range(k):
    tree[i] = (n_lst.pop(), n_lst.pop()) 