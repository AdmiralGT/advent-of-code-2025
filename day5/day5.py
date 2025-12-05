from dataclasses import dataclass

@dataclass
class FreshnessRange:
    start: int
    end: int

    def __le__(self, other):
        return self.start <= other.start
    
    def __gt__(self, other):
        return self.start > other.start
    
    def id_in_range(self, id):
        return self.start <= id <= self.end
    
    def overlap(self, other):
        if ((self.start <= other.start) and (self.end >= other.start)) or \
           ((self.start >= other.start) and (self.start <= other.end)):
           return True
        return False
    
    def extend(self, other):
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)

    def id_count(self):
        return (self.end - self.start) + 1
    
def reduce_freshness_ranges(ranges):
    ranges.sort()
    merged_ranges = []
    for freshness in ranges:
        for merged in merged_ranges:
            if freshness.overlap(merged):
                merged.extend(freshness)
                break
        else:
            merged_ranges.append(freshness)
    return merged_ranges

with open("input.txt") as f:
    lines = f.readlines()

parsing_freshness = True
fresh_ids = []
fresh = set()
rotten = set()
for line in lines:
    line = line.rstrip('\n')
    if line == '':
        parsing_freshness = False
        fresh_ids.sort()
        continue
    
    if parsing_freshness:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        fresh_ids.append(FreshnessRange(start, end))
    else:
        id = int(line)
        for freshness in fresh_ids:
            if freshness.id_in_range(id):
                fresh.add(id)
                break
        else:
            rotten.add(id)

print(f"Fresh IDs: {len(fresh)}")
print(f"Rotten IDs: {len(rotten)}")

# Merge overlapping freshness ranges

initial_range_len = 0
merged_freshness = []
while len(fresh_ids) != initial_range_len:    
    merged_freshness = reduce_freshness_ranges(fresh_ids)
    fresh_ids = merged_freshness
    initial_range_len = len(merged_freshness)

total_fresh_ids = 0
for freshness in merged_freshness:
    total_fresh_ids += freshness.id_count()

print(f"Total possible fresh IDs: {total_fresh_ids}")