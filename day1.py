# problem description: https://adventofcode.com/2023/day/1

file_path = 'inputs/1.txt'  # Replace 'your_file.txt' with the path to your file
dic = {}

dic["one"] = "1"
dic["two"] = "2" 
dic["three"] = "3"
dic["four"] = "4"
dic["five"] = "5"
dic["six"] = "6"
dic["seven"] = "7"
dic["eight"] = "8"
dic["nine"] = "9"

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = file.readlines()

def pt1():
    ans = 0
    d = ""
    for s in inp:
        d = ""
        for l in s:
            if l.isnumeric():
                d += l
                break
        for i in range(len(s)-1,-1,-1):
            l = s[i]
            if l.isnumeric():
                d += l
                break
        ans += int(d)
    return ans

def pt2():
    ans = 0    
    for s in inp:        
        d = ""
        acc = ""
        for l in s:
            acc+=l
            if l.isnumeric():
                d += l
                break

            for key in dic:
                if key in acc:
                    d = dic[key]
                    break
            if d != "": break

        acc = ""
        for i in range(len(s)-1,-1,-1):
            l = s[i]
            acc = l + acc
            if l.isnumeric():
                d += l
                break

            for key in dic:
                if key in acc:
                    d += dic[key]
                    d = int(d)
                    break
            
            if type(d) == int : break        
        ans += int(d)

    return ans

print("PART 1", pt1())
print("PART 2", pt2())