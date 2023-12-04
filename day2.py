# problem description: https://adventofcode.com/2023/day/2

file_path = 'inputs/2.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = file.readlines()

games = {}
g_id = 1
for game in inp:
    games[g_id] = {"red": 0, "green": 0, "blue": 0}
    sets = game.replace("\n", "").split(": ")[1].split("; ")
    for game_set in sets:
        colors = game_set.split(", ")
        for color in colors:
            count, c = color.split(" ")
            games[g_id][c] = max(int(count), games[g_id][c])
    g_id += 1


def pt1():
    red_max = 12
    green_max = 13
    blue_max = 14
    ans = 0
    for g_id in games:
        if games[g_id]["red"] <= red_max and games[g_id]["blue"] <= blue_max and games[g_id]["green"] <= green_max:
            ans += g_id
    return ans

def pt2():    
    ans = 0
    for g_id in games:
        ans += games[g_id]["red"] * games[g_id]["blue"] * games[g_id]["green"]         
    return ans
print("PART 1", pt1())
print("PART 2", pt2())

    