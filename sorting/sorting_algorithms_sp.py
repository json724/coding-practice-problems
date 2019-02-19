import numpy as np

def cocktail_sort(v):
    j = 0
    k = len(v)-1
    while j <= k:
        for i in range(j,k,1):
            if v[i] > v[i+1]:
                v[i], v[i+1] = v[i+1], v[i]
        for i in range(k-1,j,-1):
            if v[i] < v[i-1]:
                v[i], v[i-1] = v[i-1], v[i]
        j += 1
        k -= 1

    return v

def bubble_sort(v):
    for i in range(0,len(v)):
        for j in range(i+1,len(v)):
            if v[i] > v[j]:    
                v[i], v[j] = v[j], v[i]
    return v


def list_merge(l1,l2):
    merged_list = []
    i = 0
    j = 0
    while i<len(l1) and j<len(l2):
        
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            if l1[i] > l2[j]:
                merged_list.append(l2[j])
                j += 1
            else:
                merged_list.append(l1[i])
                merged_list.append(l2[j])
                i += 1
                j += 1
    while i<len(l1):
        merged_list.append(l1[i])
        i += 1
    while j<len(l2):
        merged_list.append(l2[j])
        j += 1
    
    return merged_list

def merge_sort(l):
    def divide(l):
        ln = len(l)
        if ln == 1 :
            return l
        else:
            l1 = divide(l[:ln//2])
            l2 = divide(l[ln//2:ln])
            return list_merge(l1,l2)
        
    return divide(l)

v1 = np.random.randint(50, size=1000)
v2 = np.random.randint(50, size=1000)
v3 = np.random.randint(50, size=1000)
cocktail_sort(v1)
bubble_sort(v2)
merge_sort(v3)