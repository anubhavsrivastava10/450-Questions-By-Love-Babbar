#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        lst = []
        for i in range(l+k):
            queue.insert(arr[i])
        lst.sort(reverse=True)
        # print(lst)
        for i in range(k,r+1):
            if lst[-1]>arr[i]:
                lst.pop(0)
                lst.append(arr[i])
        # print(lst)
        return lst[0]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends