from typing import List
import re


def split_by_pos(content: str, splitters: List[int]) -> List[str]:
    splitters = sorted(splitters)
    if splitters[0] != 0:
        splitters.insert(0, 0)
    if splitters[-1] != len(content):
        splitters.append(len(content))
    a = []
    for i in range(0, len(splitters) - 1):
        a.append(content[splitters[i]:splitters[i + 1]])
    return a


def get_pos(res: List[re.Match]):
    beg_list = []
    for i in res:
        beg = i.start()
        beg_list.append(beg)
    return beg_list
