import numpy as np
inp_prob = [0.499,	0.34,	0.161,	0.575,	0.286,	0.139]
prob = np.zeros((2,3))
print(prob)
for i in range(0,2) :
    print(i)
    prob[i][0] = inp_prob[3*i]
    prob[i][1] = inp_prob[3*i+1]
    prob[i][2] = inp_prob[3*i+2]
print(prob)
state_mapper = {'A': 0, 'B': 1}
emission_mapper = {'x':0,'y':1,'z':2}
imapper = ['A','B']
emission_inp = 'yxxyyxyzzyzxzxyzyzxzzzxyyxxzyyzyyxzyzyxxxxxxzxzzxx'
state_inp = 'ABABBBBAABABABBBABBAAABABAAABBABBBBBABBBABBABBABAB'
out = 1
for i in range (len(state_inp)) :
    out *= prob[state_mapper[state_inp[i]]][emission_mapper[emission_inp[i]]]
print(out)