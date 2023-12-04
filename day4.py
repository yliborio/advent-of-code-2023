file_path = 'inputs/4.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip() for line in file.readlines()]

cards = {}
card_id = 1
for line in inp:
    winning, owned_cards = line.split(": ")[1].split(" | ")
    cards[card_id] = {"w": set([int(x) for x in winning.split(' ') if x != '']), "c": set([int(x) for x in owned_cards.split(' ') if x != '']),"n": 1}
    card_id += 1

def pt1():
    ans = 0
    for id in cards:
        winning = len(cards[id]["w"].intersection(cards[id]["c"]))
        if winning > 0:
            ans += 2** (winning-1)
    return ans

def pt2():
    ans = 0
    for i in range(1,card_id):
        winning = len(cards[i]["w"].intersection(cards[i]["c"]))
        ans += cards[i]["n"]
        for j in range(1,winning+1):
            cards[i+ j]["n"] += cards[i]["n"]
    return ans

print("PART 1", pt1())
print("PART 2", pt2())
