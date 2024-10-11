input_string = input()
char_dict = {
    'A' : 'A',
    'G' : 'G',
    'T' : 'U',
    'C' : 'C',
}
out_put = []
for i in input_string :
    out_put.append(char_dict[i])

print("".join(map(str, out_put)))