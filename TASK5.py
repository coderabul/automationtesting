#1
string = "ABUL HASAN!"
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
print(count) 


#2
def printPattern(n):
    for i in range(1, n + 1):
        for j in range(i, n):
            print("\t", end = "")
        t = i
        for k in range (1, i + 1):
            print(t, "\t", "\t", end = "")
            t = t + n - k
print()
n = 6
printPattern(n)

#3
def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)

#4  
def countDis(str):
 
    # Stores all distinct characters
    s = set(str)
 
    # Return the size of the set
    return len(s)

S = "ABUL_HASAN"
print(countDis(S))

#5
def isPalindrome(s):
    return s == s[::-1]
 
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

#6
def LCSubStr(X, Y, m, n):
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
 
    # To store the length of
    # longest common substring
    result = 0
 
    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result
 
print('Length of Longest Common Substring is',
LCSubStr("cupcake", "cak", 7, 3))

#7
def getMaxOccurringChar(str):
    # create dictionary to store frequency of every character
    mp = {}
 
    # to store length of string
    n = len(str)
 
    # to store answer
    ans = ''
 
    # to check count of answer character is less or greater
    # than another elements count
    cnt = 0
 
    # traverse the string
    for i in range(n):
        # push element into dictionary and increase its frequency
        if str[i] in mp:
            mp[str[i]] += 1
        else:
            mp[str[i]] = 1
 
        # update answer and count
        if cnt < mp[str[i]]:
            ans = str[i]
            cnt = mp[str[i]]
 
    return ans
str = "sample string"
print("Max occurring character is:", getMaxOccurringChar(str))
