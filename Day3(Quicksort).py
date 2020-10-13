# lindex= lowerindex , hindex= higherindex
# pivot= number taken to compare


# recursive function
def quicksort(l, lindex, hindex):
    if (hindex - lindex) > 0:
        p = partition(l, lindex, hindex)
        quicksort(l, lindex, p - 1)
        quicksort(l, p + 1, hindex)


# main function
def partition(l, lindex, hindex):
    div = lindex
    pivot = hindex

    for i in range(lindex, hindex):
        if l[i] < l[pivot]:
            l[i], l[div] = l[div], l[i]
            div += 1

    l[pivot], l[div] = l[div], l[pivot]
    return div


l = list(map(int, input('Your List: ').split()))
quicksort(l, 0, len(l) - 1)
print(f"The sorted list:\n{l}")

#Output
Your List: 6 7 8 5 4 3 2 6 7 8 
The sorted list:
[2, 3, 4, 5, 6, 6, 7, 7, 8, 8]
