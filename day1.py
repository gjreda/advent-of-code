"""
https://adventofcode.com/2018/day/1

Starting with a frequency of zero, what is the resulting 
frequency after all of the changes in frequency have been 
applied?
"""

from typing import List
from collections import Counter

# part 1
def calibrate_frequency(changes: List[int], frequency: int = 0) -> int:
    return frequency + sum(changes)

assert calibrate_frequency([1, -2, 3, 1]) == 3
assert calibrate_frequency([1, 1, 1]) == 3
assert calibrate_frequency([1, 1, -2]) == 0
assert calibrate_frequency([-1, -2, -3]) == -6


# part 2
def recalibrate_frequency(changes: List[int],
                          frequency: int = 0,
                          times_seen: int = 2) -> int:
    """Recalibrate the frequency until it has reached the same value 
    the given number of times seen."""
    history = Counter([frequency])
    while True:
        for val in changes:
            frequency += val
            history.update([frequency])

            if history[frequency] == times_seen:
                return frequency
    return

assert recalibrate_frequency([1, -1], times_seen=2) == 0
assert recalibrate_frequency([3, 3, 4, -2, -4], times_seen=2) == 10
assert recalibrate_frequency([-6, 3, 8, 5, -6], times_seen=2) == 5
assert recalibrate_frequency([7, 7, -2, -7, -4], times_seen=2) == 14


if __name__ == "__main__":
    with open('inputs/day1.txt', 'r') as f:
        changes = [int(line) for line in f]
    print('Part 1: ', calibrate_frequency(changes))
    print('Part 2: ', recalibrate_frequency(changes))