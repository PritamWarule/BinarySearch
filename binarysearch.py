def binarysearch(list1,k):
    found=False
    l=len(list1)
    low=0
    high=l-1
    while low<=high and not found:
        mid=(low+high)//2
        if k==list1[mid]:
            found=True
            #print(f" Key {k} is found")
        elif k>list1[mid]:
           low=mid+1
        else:
           high=mid-1
    if found==True:
        print("key is found")
    else:
        print("key is not found")
list1=[3,2,5,4,89]
list1.sort()
k=int(input("Enter key to search: "))
binarysearch(list1,k)