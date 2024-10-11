input_dict = {}
#open the input file
with open('input.txt', 'r') as file:
    for line in file :
        stip_line = line.strip()
        if stip_line[:-1] in input_dict :
            input_dict[stip_line[:-1]].append(stip_line[1:])
        else :
            input_dict[stip_line[:-1]] = [stip_line[1:]]

sorted_keys = sorted(input_dict.keys())

# for key in sort_key :
#     print(key, "-> ", end="")
#     for item in input_dict[key][:-1] :
#         print(item, end=",")
#     print(input_dict[key][-1], end="\n")
with open('output.txt', 'w') as file:
    for key in sorted_keys:
        file.write(key + " -> ")
        for item in input_dict[key][:-1]:
            file.write(item + ", ")
        file.write(input_dict[key][-1] + "\n")