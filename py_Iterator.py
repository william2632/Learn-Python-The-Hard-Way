class PowTwo:		# class to implement an iterator of powers of two
    def __init__(self,max=0):
        self.max=max
        
    def __iter__(self):
        self.n=0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a=PowTwo(4)
i=iter(a)
print('iter:',next(i))      #1
print('iter:',next(i))      #2
print('iter:',next(i))      #4
print('iter:',next(i))      #8
print('iter:',next(i))      #16
#print('iter:',next(i))      #raise StopIteration

for i in iter(a):
    print('i=',i)
    #print('next(i)=',next(i))      #x