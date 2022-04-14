import copy

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

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