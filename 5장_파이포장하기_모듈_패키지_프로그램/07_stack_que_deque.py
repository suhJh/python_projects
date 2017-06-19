def palindrome(word):   # 앞뒤가 똑같은 문자열인지 비교하는 펑션
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True

palindrome('a')
palindrome('racecar')
palindrome('')
palindrome('radar')
palindrome('halibut')   
        

def another_palidrome(word):    # reverse와 동일
    return word == word[::-1]

another_palidrome('radar')
another_palidrome('halibut')