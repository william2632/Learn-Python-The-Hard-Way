g = [ i * 3 for i in range(10) ]
print(g)

g = ( i * 3 for i in range(10) )
print(g)
print( next (g) )
print( next (g) )
print( next (g) )
print( next (g) )

print('------define yield.')
def gtr(n):
    for i in range(n):
        yield i


r=gtr(3)
print(next(r))
print(next(r))
print(next(r))
#print(next(r))

print('------define yield test.')
def test():
    n = 0
    while True:
        if n < 3:
            yield n
            n += 1
        else:
            yield 10

t=test()
for i in range(6):
    print(next(t))

print('------define yield from.')

def g1():
    yield range(5)
def g2():
    yield from range(5)

it1=g1()
it2=g2()
print('----yield:')
for x in it1:
    print(x)
print('----yield from:')
for x in it2:
    print(x)


# 最后，我们来看一个yield from使用的一个经典场景：二叉树的遍历：
print('binary tree:')
class Node:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
        self.iterated=False
        self.father=None
    def iterate(self):
        if self.lchild is not None:
            yield from self.lchild.iterate()
        print(self.key)
        yield self.key
        if self.rchild is not None:
            yield from self.rchild.iterate()

class Tree:
    def __init__(self):
        self.root=Node(4)
        self.root.lchild=Node(3)
        self.root.lchild.father=self.root
        self.root.rchild=Node(5)
        self.root.rchild.father=self.root
        self.root.lchild.lchild=Node(1)
        self.root.lchild.lchild.father=self.root.lchild
        self.root.rchild.rchild=Node(7)
        self.root.rchild.rchild.father=self.root.rchild
    
    def iterate(self):
        yield from self.root.iterate()

T=Tree()
T.iterate()