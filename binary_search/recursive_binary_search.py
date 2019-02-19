
def search(a,k,l,r):
    l = 0
    r = len(a)
    mid = (r-l)//2
    
    if r <= l:
        return False
    if k == a[mid]:
        return True
    if k < a[mid]:
        r = mid
    if k > a[mid]:
        l = mid+1
    return search(a[l:r], k, l, r)

if __name__ == "__main__":
    arr = [-12,-1,2,3,6,8,10,15,22,45,67,245]
    k = 15

    l = 0 #Left
    r = len(arr) #Right
    print(search(arr,k,l,r))