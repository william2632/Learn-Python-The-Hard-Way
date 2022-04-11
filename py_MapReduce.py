from collections import Counter, defaultdict
from functools import reduce
import numpy as np
texts=['apple bear peach grape', 'grape orange peach']

#convert string to list, every word is 1
def mp1(text):
    ret=[]
    words = text.split(' ')
    for word in words:
        ret.append((word,1))
    #print(*ret,sep="\n")
    #print('--'.join(ret))
    #print(ret[0:])
    #print(ret)
    return ret

'''
testList=[]
#returnList=[]
print('----start loop')
for text in texts:
    #returnList.append(mp1(text))
    mp1(text)
#print('returnList:',returnList)
print('testList:',testList)

testList=[]
#returnList2=[]
print('----start map')
#returnList2=list(map(mp1,texts))
#print('returnList2:',returnList2)
map(mp1,texts)
print('testList:',list(map(mp1,texts)))
'''

#convert list to dict
def mp2(arr):
    d=defaultdict(int)
    for k,v in arr:
        print('k=',k,';v=',v)
        d[k] += v
    return d

'''
print('----start Loop2')
for l in testList:
    print(mp2(l))
print('----start map2')
print(list(map(mp2,testList)))
'''
print('----start mp2')
print(list(map(mp2,map(mp1,texts))))

#reduce, combine dict
def rd(x,y):
    #print('x=',x,';y=',y)
    x.update(y)
    return(x)

print('----start reduce')
print(reduce(rd,map(mp2,map(mp1,texts))))

