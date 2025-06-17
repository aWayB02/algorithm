def merge(a, b):

    left = 0
    right = 0
    ans = []

    while left < len(a) and right < len(b):

        if a[left] > b[right]:

            ans.append(b[right])
            right += 1

        elif a[left] <= b[right]:
            ans.append(a[left])
            left += 1

    while left < len(a):
        ans.append(a[left])
        left += 1

    while right < len(b):
        ans.append(b[right])
        right += 1

    return ans


def sort(a):

    if len(a) <= 1:
        return a

    mid = len(a) // 2
    al = sort(a[:mid])
    ar = sort(a[mid:])
    return merge(al, ar)


print(sort([3, 2, 1]))
