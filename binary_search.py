def binary_search(a,search):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = start + (end-start)//2
        if a[mid] == search:
            return mid
        else:
            if a[mid]>search:
                end = mid - 1
            else:
                start = mid + 1
    return 'None'

a = [1,2,3,5,6,9,10,15,20,36,36,39,45,47,53,56,68,70,74,75,79,89,90]
search = 38
binary_search(a,search)