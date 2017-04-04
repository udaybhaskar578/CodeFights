'''
Author: Sai Uday Bhaskar Mudivarty
Question: https://codefights.com/interview/qAL6AiSejoJZRNyox/description
'''
def sumOfTwo(a, b, v): 
    b = set(b)
    for i in a:
        k = v-i
        try:
            if k in b:
                
                return True
        except ValueError:
            continue 
    return False
