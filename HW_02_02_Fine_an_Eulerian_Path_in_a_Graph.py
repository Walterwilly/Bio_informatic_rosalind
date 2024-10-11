# check that one euler path exist
# starting node have out_degree - in_degree = 1
# ending node have in_degree - out_degree = 1
# other have in_degree = out_degree
def parse_input(input_file) :
    out_put = {}
    num_deg = {}
    starter = set({})
    with open(input_file, 'r') as file :
        for line in file :
            line = line.strip()
            if line :
                parts = line.split(' -> ')
                vertex = int(parts[0])
                if(parts[1]) :
                    edges = list(map(int, parts[1].split(',')))
                    if vertex in num_deg :
                        if num_deg[vertex] == -1 :
                            starter.remove(vertex)
                        num_deg[vertex] -= len(edges)
                    else :
                        num_deg[vertex] = -len(edges)
                    if num_deg[vertex] == -1 :
                        starter.add(vertex)
                    for item in edges :
                        if item in num_deg :
                            if num_deg[item] == -1 :
                                starter.remove(item)
                            num_deg[item] += 1
                        else :
                            num_deg[item] = 1
                        if num_deg[item] == -1 :
                            starter.add(item)
                else :
                    edges = []
                out_put[vertex] = edges
    return out_put, list(starter)[0]

def find_eulerain_path(adj, start) :
    stack = [start]
    path = []
    while stack :
        v = stack[-1] 
        if v in adj and adj[v] :
            next_v = adj[v].pop()
            stack.append(next_v)
        else :
            path.append(stack.pop())
    return path

file_graph, starter = parse_input('input.txt')
rpath = find_eulerain_path(file_graph, starter)
path = rpath[::-1]
print(path)
with open('output.txt', 'w') as file:
    for item in path[:-1] :
        file.write(str(item)+"->")
    file.write(str(path[-1]))
