input_text = input()
char_count = {
    'A' : 0,
    'C' : 0,
    'G' : 0,
    'T' : 0
}
for i in input_text :
    char_count[i] += 1

for i in char_count :
    print(char_count[i], end=' ')