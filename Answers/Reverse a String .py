#User function Template for python3

def reverseWord(s):
    #your code here
    start = 0
    end = len(s)
    while start <= end:
        s[start],s[end-1] = s[end-1],s[start]
        start+=1
        end -=1
    return s
    
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends