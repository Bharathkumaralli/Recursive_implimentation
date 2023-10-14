def Binary_search(arr,target,l,r):
    if r>l:
        mid = (l+r)//2
    
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return Binary_search(arr,target,mid,r)
        else :
            return Binary_search(arr,target,l,mid) 
    else :
        return -1
