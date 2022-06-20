import copy
import pandas as pd

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

'''
print("Guru99_01")
l=[i for i in range(3,9)]
print(l)

E0 = [[1, 2, 3,4], [ 5, 6,7,8], [9,10,12,11]]
E0_copy = E0
E1_copy = list(E0)
E3_copy = copy.deepcopy(E0)
E4_copy = E0[:]
ES=E0[:]
E0=sorted(E0)

print('E0:',E0)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E0_c:',E0_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E1_c:',E1_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E3_c:',E3_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E4_c:',E4_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('ES:',ES)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]

E0_copy[0][0] = 0
E1_copy[1][1] = 0
E3_copy[2][3] = 111
E4_copy[0][3] = 999

print('E0:',E0)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E0_c:',E0_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E1_c:',E1_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E3_c:',E3_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('E4_c:',E4_copy)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
print('ES:',ES)  # -> [[0, 2, 3], [4, 0, 6], [7, 8, 0]]



numbers=[12, 5, 34, 11]
print('numbers:',numbers)
backUp = numbers[:]                     # this is link, not deep copy
numbers = sorted(numbers)               # but sorted created a deep copy
print('numbers after sort:',numbers)
print('backUp:',backUp)

s='012345'
print(s[:3])

f='filename.ext'
print(f[:-5])

#define result location
path = r'D:\powershell'
#files = os.listdir(path)
#reading sheets
#for file in files:
file='processes_0418.xlsx'
df_temp = pd.read_excel(path +"\\"+file, skiprows=6,usecols='A:G').dropna()
df_temp['Filename'] = file[:-5]
print(df_temp)
'''

# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    #for arg in kwargs.values():
    #    result += arg
    argTuples=kwargs.items()
    print(argTuples)
    for aT in argTuples:
        print(aT)
    print(type(kwargs.items()))
    print(type(kwargs.keys()))
    print(type(kwargs.values()))
    print(' '.join(kwargs.keys()))
    result = ' '.join(kwargs.values())
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


def updatelist(li):
    print(type(li))
    li[0]='x'
    return

my_list = [1, 2, 3]
print(my_list)
print(*my_list)
updatelist(my_list)
print(my_list)

def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)
#my_sum(my_list)


my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a,type(a))
print(b,type(b))
print(c,type(c))

*a, = "RealPython"
print(a,type(a))

print('2022-06-19')
