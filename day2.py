"""
https://adventofcode.com/2018/day/2
"""

from typing import List, Dict, Tuple
from collections import defaultdict


def count_letters(s: str) -> Dict[str, int]:
    counts = defaultdict(int)
    for letter in s:
        counts[letter] += 1
    return counts

# Part 1
def checksum(box_ids: List[str]) -> int:
    two_letter_count = 0
    three_letter_count = 0

    for id_ in box_ids:
        letter_counts = count_letters(id_)

        if 2 in letter_counts.values():
            two_letter_count += 1
        if 3 in letter_counts.values():
            three_letter_count += 1
    return two_letter_count * three_letter_count


box_ids = ['abcdef', 'bababc', 'abbcde', 'abcccd',
           'aabcdd', 'abcdee', 'ababab']
assert checksum(box_ids) == 12


# Part 2
def differ_by_one_char(word1: str, word2: str):
    """Returns the common letters if the two words differ by one char."""
    # Box IDs should be the same length
    if len(word1) != len(word2):
        return False
    
    different_count = 0
    common_letters = ''
    for s1, s2 in zip(word1, word2):
        if s1 == s2:
            common_letters += s1
        else:
            different_count += 1

        if different_count > 1:
            break
    return common_letters if different_count == 1 else False


assert differ_by_one_char('abcdef', 'abc') == False
assert differ_by_one_char('abcdef', 'abcdef') == False
assert differ_by_one_char('abcdef', 'abcdgg') == False
assert differ_by_one_char('abcdef', 'abcdeg') == 'abcde'
assert differ_by_one_char('abcdef', 'axcdef') == 'acdef'


if __name__ == "__main__":
    with open('inputs/day2.txt', 'r') as f:
        box_ids = [line for line in f]
    print('Part 1: ', checksum(box_ids))

    # this seems not ideal, but first, make it right, then make it fast
    for id1 in box_ids:
        for id2 in box_ids[1:]:
            common_letters = differ_by_one_char(id1, id2)
            if common_letters:
                print(common_letters)
                break