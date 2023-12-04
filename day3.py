# problem description: https://adventofcode.com/2023/day/3

file_path = 'inputs/3.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip() for line in file.readlines()]


# save numbers position in matrix: {row: [(col_i,col_j),...]}
numbers = {}


def check_adj_symbols(px,py):
    i,j = px
    _, l = py
    num = ""
    for di in range(j,l):
        num += inp[i][di]
    
    num = int(num)
    found_symbol = False
    ## checks adjacent positions for number
    for ai in range(i-1,i+2):
        if ai < 0: continue
        if ai >= len(inp): continue
        for aj in range(j-1,l+1):
            if aj < 0: continue
            if aj >= len(inp[0]): continue
            c = inp[ai][aj]
            if c != '.' and not c.isnumeric():
                found_symbol = True
                break
        if found_symbol: break
    if found_symbol:        
        return num
    return 0



def pt1():
    rows = len(inp)
    cols =  len(inp[0])    
    ans = 0
    for i in range(rows):
        num = None
        for j in range(cols):

            if inp[i][j].isnumeric() and num == None:
                # found first digit of number
                num = (i,j)
            else:
                # check if number was read
                if num != None and not inp[i][j].isnumeric():                    
                    numbers[i] = numbers.get(i,[]) + [(num[1],j)] 
                    # if has adjacent symbol add it to answer, else sums 0
                    ans += check_adj_symbols(num, (i,j))
                    num = None
        if num != None:
                # corner case to number in last col
                numbers[i] = numbers.get(i,[]) + [(num[1],cols)] 
                ans += check_adj_symbols(num, (i,cols))
                num = None                        
    return ans

def pt2():
    rows = len(inp)
    cols =  len(inp[0])
   
    ans = 0
    for i in range(rows):   
        for j in range(cols):

            if inp[i][j] == "*":
                ## found * symbol
                adj = []

                ## check for adjacent numbers
                for k in range(i-1,i+2):                
                    if k not in numbers: continue                    
                    for num in numbers[k]:
                        ci, cj = num                        
                        if (ci >= j-1 and ci <= j+1) or (cj-1 >= j-1 and cj <= j+1):
                            adj.append((k,num))
                # if found 2, add ratio to answer
                if len(adj) == 2:
                    ratio = 1
                    for num in adj:
                        r = num[0]
                        ci,cj = num[1]
                        ratio *= int(inp[r][ci:cj])
                    ans += ratio
    return ans

print("PART 1", pt1())
print("PART 2", pt2())

    