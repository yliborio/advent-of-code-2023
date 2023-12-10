file_path = 'inputs/7.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip() for line in file.readlines()]


from enum import Enum

class PokerHandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

class CardValue(Enum):
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10    
    


class Game:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
    
    def __lt__(self, other):
        r1, r2 = get_hand_rank(self.hand).value, get_hand_rank(other.hand).value
        if r1 != r2:
            return r1 < r2

        h1,h2 = self.hand, other.hand
        for i in range(len(h1)):
            c1 = get_card_value(h1[i])
            c2 = get_card_value(h2[i])
            if c1 != c2: return c1 < c2
        return False
    
class Game2(Game):
    def __lt__(self, other):
        r1, r2 = get_hand_rank_with_joker(self.hand).value, get_hand_rank_with_joker(other.hand).value
        if r1 != r2:
            return r1 < r2

        h1,h2 = self.hand, other.hand
        for i in range(len(h1)):
            c1 = get_card_value(h1[i]) if h1[i] != "J" else 1
            c2 = get_card_value(h2[i]) if h2[i] != "J" else 1
            if c1 != c2: return c1 < c2
        return False

            


cards = []
cards2 = []
for line in inp:
    card, bid = line.split()
    cards.append(Game(card,int(bid)))
    cards2.append(Game2(card,int(bid)))


def get_hand_rank(hand):
    card_count = {}
    for l in hand:
        card_count[l] = card_count.get(l,0) + 1
    counts = card_count.values()
    if len(card_count) == 1:
        return PokerHandType.FIVE_OF_A_KIND
    if len(card_count) == 2:
        if 4 in counts:
            return PokerHandType.FOUR_OF_A_KIND
        return PokerHandType.FULL_HOUSE
    if len(card_count) == 3:
        if 3 in counts:
            return PokerHandType.THREE_OF_A_KIND
        return PokerHandType.TWO_PAIR
    if len(card_count) == 4:
        return PokerHandType.ONE_PAIR
    return PokerHandType.HIGH_CARD

def get_hand_rank_with_joker(hand):
    rank = get_hand_rank(hand)
    jokers = hand.count("J")
    if jokers == 0 or jokers == 5: return rank
    if jokers == 1:
        if rank == PokerHandType.FOUR_OF_A_KIND: return PokerHandType.FIVE_OF_A_KIND
        if rank == PokerHandType.FULL_HOUSE: return PokerHandType.FOUR_OF_A_KIND
        if rank == PokerHandType.THREE_OF_A_KIND: return PokerHandType.FOUR_OF_A_KIND
        if rank == PokerHandType.TWO_PAIR: return PokerHandType.FULL_HOUSE
        if rank == PokerHandType.ONE_PAIR: return PokerHandType.THREE_OF_A_KIND
        if rank == PokerHandType.HIGH_CARD: return PokerHandType.ONE_PAIR
    if jokers == 2:
        if rank == PokerHandType.FULL_HOUSE: return PokerHandType.FIVE_OF_A_KIND        
        if rank == PokerHandType.TWO_PAIR: return PokerHandType.FOUR_OF_A_KIND
        if rank == PokerHandType.ONE_PAIR: return PokerHandType.THREE_OF_A_KIND        
        return rank    
    if jokers == 3:
        if rank == PokerHandType.FULL_HOUSE: return PokerHandType.FIVE_OF_A_KIND    
        if rank == PokerHandType.THREE_OF_A_KIND: return PokerHandType.FOUR_OF_A_KIND                  
    return PokerHandType.FIVE_OF_A_KIND

def get_card_value(card):    
    if card.isnumeric():
        return int(card)         
    return CardValue[card].value         


def pt1():
    ans = 0
    sorted_card_values = sorted(cards)    
    rank = 1        
    for game in sorted_card_values:
        ans += game.bid * rank        
        rank += 1
    return ans

def pt2():
    ans = 0    
    sorted_card_values = sorted(cards2)    
    rank = 1        
    for game in sorted_card_values:
        ans += game.bid * rank        
        rank += 1
    return ans
    
print("PART 1", pt1())
print("PART 2", pt2())