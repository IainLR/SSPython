# 1
from typing import Reversible


print('Hello World'[8])

# 2
print('thinker'[2:5])

# 3
s = 'sammy'
print(s[2:])

# 4
print(set('Mississippi'))

# 5
phrases = ['Stars', 'O, a kak Uwakov lil vo kawu kakao!', 'Some men interpret nine memos']
def palindrome_test(numOfPhrases, arrOfPhrases):
    resultString = ""
    for i in range(numOfPhrases):
        modString = arrOfPhrases[i].replace(" ", "").replace("!","").replace(",", "").lower()
        if modString == modString[::-1]:
            resultString += "Y "
        else:
            resultString += "N "
        
    print(resultString) 

palindrome_test(3, phrases)  


