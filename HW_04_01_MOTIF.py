import numpy as np
arr = []
num = 0
km = 10 #k-mer
with open('input.txt','r') as file :
    first_line = file.readline().strip()
    km, num = map(int, first_line.split())  # Split the first line into two integers

    # Now iterate over the remaining lines to get sequences
    for line in file:
        arr.append(line.strip())  # Strip to remove any trailing newline or spaces
dimap = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3} # a c g t

def scoring(vec) : # dimension 1 x 97
    out_score = 0
    for i in range(km) :
        score = [0, 0, 0, 0]
        for j in range(len(vec)) :
            score[dimap[vec[j][i]]] += 1
        out_score += 97-max(score)
    return out_score
        
def profile_cal(vec) : # return metrix and maximum score
    out_v = np.zeros((4,km))
    for i in range(len(vec)) : # number of read
        for j in range(km) :
            out_v[dimap[vec[i][j]]][j] += 1
    out_v = (out_v+1)/len(vec)
    return out_v, scoring(vec)

def forever(vec, score_vec) : # return new profile_arr
    new_profile_arr = []
    for i in range(len(vec)) :
        outstring = ""
        maxpop = 0
        for j in range(len(vec[i])-km+1) :
            temp_score = 1
            for z in range(km) :
                temp_score *= score_vec[dimap[vec[i][j+z]]][z]
            if(temp_score > maxpop) :
                maxpop = temp_score
                outstring = vec[i][j:j+km]
        new_profile_arr.append(outstring)
    return new_profile_arr

#initiate first profile arr
best_score = 10000000000
profile_arr = []
for e in arr :
    profile_arr.append(e[0:0+km])
svec, outs = profile_cal(profile_arr)
#while loop
while True :
    profile_arr = forever(arr, svec)
    svec, outs = profile_cal(profile_arr)
    if(outs < best_score) :
        best_score = outs
    else :
        break
with open('output.txt','w') as file :
    for i in range(len(profile_arr)) :
        file.write(f'{profile_arr[i]}\n')
with open('output2.txt','w') as file :
    for i in range(len(arr)) :
        os = arr[i].replace(profile_arr[i],profile_arr[i].upper())
        file.write(f'>test{i+1}\n{os}\n')