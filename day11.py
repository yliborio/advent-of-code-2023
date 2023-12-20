import itertools
import heapq

file_path = 'inputs/11.txt'
positions = {}
cols = set([])
rows = set([])
weight_map = []
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = []
    count = 1
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()    
        for j in range(len(line)):
            if line[j] == '#':
              positions[count] = (i,j)
              count += 1
              cols.add(j)
              rows.add(i)                          
        inp.append([l for l in line])

pairs = list(itertools.combinations(range(1,count), 2))
for i in range(len(inp)):
    line_weight = []
    for j in range(len(inp[0])):
        if j in cols and i in rows: 
            line_weight.append(1)
        else:
            line_weight.append(2)
    weight_map.append(line_weight)


#djisktra
def calculate_weighted_distance(point_a):
    priority_queue = [(0, point_a)]
    visited = set()

    distances = {}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        distances[current_vertex] = current_distance
        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        neighbors = [((current_vertex[0] + directions[i][0]), current_vertex[1] + directions[i][1]) for i in range(len(directions))]
        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[0] >= len(inp) or neighbor[1] < 0 or neighbor[1] >= len(inp):
                continue
        
        
            if neighbor not in visited:
                total_distance = current_distance + weight_map[neighbor[0]][neighbor[1]]
                heapq.heappush(priority_queue, (total_distance, neighbor))

    return distances


def pt1():
    ans = 0    
    all_distances = precompute_distances()
    for i in range(len(pairs)): 
        pair = pairs[i] 
        distance = all_distances[positions[pair[0]]]  
        ans += distance[positions[pair[1]]]
    return ans

def pt2():
    global weight_map
    for i in range(len(weight_map)):
        for j in range(len(weight_map[0])):
            if weight_map[i][j] > 1:
                weight_map[i][j] = 1000000
    all_distances = precompute_distances()
    ans = 0
    for i in range(len(pairs)): 
        pair = pairs[i] 
        distance = all_distances[positions[pair[0]]]  
        ans += distance[positions[pair[1]]]
    return ans

def precompute_distances():
    all_distances = {}
    for i in range(1,count):
        all_distances[positions[i]] = calculate_weighted_distance( positions[i])
    return all_distances


print("PART 1", pt1())
print("PART 2", pt2())


