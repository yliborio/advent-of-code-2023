file_path = 'inputs/9.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip().split() for line in file.readlines()]

sequences = [list(map(int, inp[i])) for i in range(len(inp))]


def predict(sequence, backwards=False):
    if set(sequence) == set([0]) :
        return 0
    subseq = []
    for i in range(len(sequence) -1):
        subseq.append(sequence[i+1] - sequence[i])
    
    if backwards:
        return sequence[0] - predict(subseq, True) 
    return sequence[-1] + predict(subseq)

def pt1():
    return sum([predict(seq) for seq in sequences])
def pt2():
    return sum([predict(seq, True) for seq in sequences])

print("PART 1", pt1())
print("PART 2", pt2())
