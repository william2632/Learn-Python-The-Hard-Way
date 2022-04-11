from collections import Counter, defaultdict
from functools import reduce
import numpy as np
texts=['apple bear peach grape', 'grape orange peach']

#convert string to list, every word is 1
def mp(text):
    words = text.split(' ')
    return Counter(words)

print('----start map')
returnList=list(map(mp,texts))
print('returnList:',returnList)

print(reduce(lambda x,y:x+y,map(mp,texts)))

