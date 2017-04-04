'''
Author: Sai Uday Bhaskar Mudivarty
Question: https://codefights.com/interview/MZnrYnavhHmYEwZs8/description
Time Complexity: O(n^2)
'''
def tripletSum(x, a):
    a = sorted(a)
    for i in range(0,len(a)-2):
        l = i+1
        r = len(a)-1
        while l<r:
            if a[i]+a[l]+a[r] == x:
                return True
            elif a[i]+a[l]+a[r] < x:
                l+=1
            else:
                r-=1
    return False
        

