from typing import List


file_path = 'inputs/5.txt'
with open(file_path, 'r') as file:
    # Read all lines from the file and create an array of strings
    inp = [line.strip() for line in file.readlines()]

class RangeInfo:
    def __init__(self, dest, source, length):
        self.dest = dest
        self.source = source
        self.length = length
    def __str__(self):
        return f"RangeInfo(lo={self.lo}, hi={self.hi}, length={self.length})"
    

seeds = []
soil : List[RangeInfo] = []
fertilizer : List[RangeInfo]  = []
water : List[RangeInfo]  = []
light : List[RangeInfo]  = []
temperature : List[RangeInfo]  = []
humidity : List[RangeInfo]  = []
location : List[RangeInfo]  = []

# Parse seeds
seeds_line = inp[0].split(': ')[1]
seeds = list(map(int, seeds_line.split()))


# Parse seed-to-soil map
i = 3
count = 0
while inp[i] != "":
    soil_line = inp[i].split()
    soil.append(RangeInfo(*list(map(int, soil_line))))
    i+=1
i+=2
# Parse soil-to-fertilizer map
while inp[i] != "":
    fertilizer_line = inp[i].split()
    fertilizer.append(RangeInfo(*list(map(int, fertilizer_line))))
    i+=1
i+=2
# Parse fertilizer-to-water map
while inp[i] != "":
    water_line = inp[i].split()
    water.append(RangeInfo(*list(map(int, water_line))))
    i+=1
i+=2
# Parse water-to-light map
while inp[i] != "":
    light_line = inp[i].split()
    light.append(RangeInfo(*list(map(int, light_line))))
    i+=1
i+=2
# Parse light-to-temperature map
while inp[i] != "":
    temperature_line = inp[i].split()
    temperature.append(RangeInfo(*list(map(int, temperature_line))))
    i+=1
i+=2
# Parse temperature-to-humidity map
while inp[i] != "":
    humidity_line = inp[i].split()
    humidity.append(RangeInfo(*list(map(int, humidity_line))))
    i+=1
i+=2
# Parse humidity-to-location map
while i < len(inp):
    location_line = inp[i].split()
    location.append(RangeInfo(*list(map(int, location_line))))
    i+=1


def convert(value: int, map_list: List[RangeInfo] ):        
    for range_info in map_list:
        if value >= range_info.source and value < range_info.source + range_info.length:
            aux = range_info.dest + value - range_info.source
            return aux
    return value

def get_ranges(value: int ): 
    range_list = [soil, fertilizer,water,light,temperature,humidity,location] 
    ans = (0,float("inf"))
    for map_list in range_list:      
        for range_info in map_list:
            if value >= range_info.source and value < range_info.source + range_info.length:
                value = range_info.dest + value - range_info.source
                ans = (max(ans[0],range_info.source), min(ans[1],range_info.source + range_info.length))         
                break
    return ans



def pt1():
    locations = []
    for seed in seeds:
        locations.append(convert(convert(convert(convert(convert(convert(convert(seed,soil), fertilizer),water),light),temperature),humidity),location))    
    return min(locations)

def pt2():
    raise("not implemented yet :(" )
        

print("PART 1", pt1())
print("PART 2", pt2())