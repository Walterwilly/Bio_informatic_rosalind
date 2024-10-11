import numpy as np
prob = [[0.806, 0.194],[0.623, 0.377]]
mapper = {'A': 0, 'B': 1}
imapper = ['A','B']
inp = 'BABBBBAAABBABBBAABBABBBABBBABAABAABBBAAABBAAABBBBB'
out = 0.5
for i in range (len(inp)-1) :
    out *= prob[mapper[inp[i]]][mapper[inp[i+1]]]
print(out)