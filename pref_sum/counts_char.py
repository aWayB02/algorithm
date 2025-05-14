"""
prefix frequency arrays
"""

from string import ascii_lowercase as abc

s = "abcd"
prefix_freq = [[0] * 26]

for ch in s:
    current = prefix_freq[-1].copy()
    current[ord(ch) - ord("a")] += 1
    prefix_freq.append(current)


def get_freq(l, r, prefix_freq):
    return [prefix_freq[r][i] - prefix_freq[l - 1][i] for i in range(26)]


for i, freq in enumerate(get_freq(3, 4, prefix_freq)):
    if freq:
        print(f"{abc[i]}: {freq}")
