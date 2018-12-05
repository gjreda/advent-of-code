"""
https://adventofcode.com/2018/day/3

This code is nasty, but it works and it is right.
Don't judge me for it.
"""

from typing import List, Dict, Any
from collections import defaultdict
import re

def parse_claim(claim: str) -> Dict[str, Any]:
    claim_id = re.findall(r'#([0-9]+) @', claim)[0]
    left, top = re.findall(r'@ ([0-9]+),([0-9]+):', claim)[0]
    width, height = re.findall(r': ([0-9]+)x([0-9]+)', claim)[0]
    return {'id': claim_id,
            'left_pad': int(left),
            'top_pad': int(top),
            'width': int(width),
            'height': int(height)}


# code's a mess. don't care. these challenges are for fun.
def calculate_overlap(claims: List[str]) -> int:
    grid = defaultdict(list)
    overlap = 0

    for claim in claims:
        parsed = parse_claim(claim)

        left = parsed['left_pad']
        width = parsed['width']
        top = parsed['top_pad']
        height = parsed['height']

        for i in range(left, left + width, 1):
            for j in range(top, top + height, 1):
                grid[(i, j)].append(parsed['id'])

                # only add when it is claimed twice
                # if > 1 == we would over count on 3, 4, 5 ...
                if len(grid[i, j]) == 2:
                    overlap += 1
    return grid, overlap


claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
grid, overlap = calculate_overlap(claims)
assert overlap == 4


if __name__ == "__main__":
    with open('inputs/day3.txt', 'r') as f:
        claims = [line for line in f]
    
    grid, overlap = calculate_overlap(claims)

    all_claims = set()
    overlapped_claims = set()
    for axes, ids in grid.items():
        if len(ids) > 1:
            for claim in ids:
                overlapped_claims.add(claim)
        for claim in ids:
            all_claims.add(claim)

    print('Part 1: ', overlap)
    print('Part 2: ', all_claims.difference(overlapped_claims))