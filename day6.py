file_path = 'inputs/6.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip() for line in file.readlines()]

times = list(map(int,inp[0].split()[1:]))
records = list(map(int,inp[1].split()[1:]))

def pt1():
    ans = 1
    for i in range(len(times)):
        time = times[i]
        record= records[i]
        win = 0
        for speed in range(1,time):
            if speed * (time - speed) > record: win +=1
        if win > 0: ans *= win
    return ans


def pt2():
    ans = 1
    time = int(''.join([str(t) for t in times]))
    record= int(''.join([str(r) for r in records]))
    ans = 0
    for speed in range(1,time):
        if speed * (time - speed) > record: ans +=1 
    return ans

print("PART 1", pt1())
print("PART 2", pt2())

