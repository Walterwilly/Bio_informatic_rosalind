import numpy as np
gap = 1
match = 3
mismatch = -3
string01 = ""
string02 = ""
with open('input.txt','r') as file :
    lines = file.readlines()
    string02 = lines[0].strip()
    string01 = lines[1].strip()
# string02 = 'TGTTACGG'
# string01 = 'GGTTGACTA'
arr = np.zeros((len(string01)+1,len(string02)+1))
for i in range(len(string01)+1) :
    arr[i][0] = i
for j in range(len(string02)+1) :
    arr[0][j] = j
for i in range(1, len(string01)+1) :
    for j in range(1, len(string02)+1) :
        if(string01[i-1] == string02[j-1]) :
            arr[i][j] = arr[i-1][j-1]
        else :
            r0 = arr[i-1][j-1]+1
            r1 = arr[i][j-1]+1
            r2 = arr[i-1][j]+1
            arr[i][j] = min([r0,r1,r2])
print(arr[-1][-1])