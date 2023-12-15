import math

class Node:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right

file_path = 'inputs/8.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip() for line in file.readlines()]


instructions = inp[0]

network = {}
for i in range(2,len(inp)):
    line = inp[i]
    value, lr = line.split(" = ")
    l,r = lr.replace("(", "").replace(")", "").split(", ")
    network[value] = Node(value,l,r)

def startsWith(letter):
    ans = []
    for node in network:
        if node[-1] == letter:
            ans.append(network[node])
    return ans


def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.lcm(result, num)
    return result

def pt1():
    curr = network["AAA"]
    step = 0
    n = len(instructions)
    while curr.value != "ZZZ":
        ins = instructions[step%n]
        curr = network[curr.left] if ins == "L" else network[curr.right]
        step += 1
    return step


def pt2():
    curr = startsWith("A")     
    step = 0
    n = len(instructions)
    found = {}
    while len(found) < len(curr):        
        ins = instructions[step%n]         
        for i in range(len(curr)):
            node = curr[i].value
            if node[2] == "Z" and node not in found:
                found[node] = step                
            curr[i] = network[curr[i].left] if ins == "L" else network[curr[i].right]
        step += 1
          
    return lcm_of_list(list(found.values()))

print("PART 1", pt1())
print("PART 2", pt2())
