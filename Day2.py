def linear_search(l: list, n):
    for i in l:
        if i == n:
            pos = l.index(i)
            return pos


def binary_search(b: list, n):
    b.sort()
    upper = len(b) - 1
    lower = 0
    while True:
        ul = upper + lower
        mid = ul // 2
        if n == b[mid]:
            print(f'Binary Search:\nFound in index {mid}')
            return True
        elif n < b[mid]:
            upper = mid - 1
            ul = upper + lower
            mid = ul // 2
        elif n > b[mid]:
            lower = mid + 1
            ul = upper + lower
            mid = ul // 2


l = list(map(int, input('Your List: ').split()))
n = int(input('No. to find: '))
if linear_search(l, n):
    print(f'Linear Search:\nFound in index {linear_search(l, n)}')
else:
    print('Not Found')
binary_search(l, n)
